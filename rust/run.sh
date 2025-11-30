#!/usr/bin/env bash
set -euo pipefail

if ! command -v cargo >/dev/null 2>&1; then
    echo "cargo is required to run Rust solutions" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUST_DIR="${SCRIPT_DIR}"
REPO_ROOT="$(cd "${RUST_DIR}/.." && pwd)"

year=$(date +"%Y")
day=$(date +"%d")
extra=""

while getopts "y:d:e:" flag; do
    case "${flag}" in
        y) year=${OPTARG} ;;
        d) day=${OPTARG} ;;
        e) extra=${OPTARG} ;;
    esac
done

if [[ -z "${year}" || -z "${day}" ]]; then
    echo "Year and day must be provided" >&2
    exit 1
fi

day=$(printf "%02d" "${day}")
prefix="day${day}"
suffix=""
if [[ -n "${extra}" ]]; then
    suffix="_${extra}"
fi

bin_name="y${year}d${day}${suffix}"
target_file="${RUST_DIR}/solutions/${year}/day${day}${suffix}.rs"

if [[ ! -f "${target_file}" ]]; then
    echo "Rust source not found: ${target_file}" >&2
    exit 1
fi

input_dir="${REPO_ROOT}/input/${year}"
if [[ ! -d "${input_dir}" ]]; then
    echo "Input directory not found: ${input_dir}" >&2
    exit 1
fi

shopt -s nullglob
files=("${input_dir}/${prefix}"*.txt)
shopt -u nullglob

if [[ ${#files[@]} -eq 0 ]]; then
    echo "No inputs found for ${year} ${prefix}" >&2
fi

if [[ ${#files[@]} -gt 0 ]]; then
    IFS=$'\n' files=($(printf '%s\n' "${files[@]}" | sort))
    unset IFS
else
    files=()
fi

labels=()
for path in "${files[@]}"; do
    name="${path##*/}"
    right="${name#${prefix}}"
    if [[ "${right}" == _* ]]; then
        label="${right:1}"
        labels+=("${label%%.*}")
    else
        labels+=("input")
    fi
done

printf '%s\n' "${bin_name}"
for part in part1 part2; do
    printf '%s %s %s\n' "------------" "${part}" "------------"
    for i in "${!files[@]}"; do
        label="${labels[$i]}"
        path="${files[$i]}"
        printf '%-10s: ' "${label}"
        start_ns=$(date +%s%N)
        if output=$(cargo run --manifest-path "${RUST_DIR}/Cargo.toml" --quiet --bin "${bin_name}" -- "${part}" "${path}" 2>&1); then
            end_ns=$(date +%s%N)
            elapsed=$(awk -v start="${start_ns}" -v end="${end_ns}" 'BEGIN { printf "%.3f", (end-start)/1000000 }')
            printf '%10s [%s ms]\n' "${output}" "${elapsed}"
        else
            echo "error"
            printf '%s\n' "${output}" >&2
        fi
    done
    echo
done
