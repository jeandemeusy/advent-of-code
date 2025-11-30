#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RUST_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
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

day=$(printf "%02d" "${day}")
suffix=""
if [[ -n "${extra}" ]]; then
    suffix="_${extra}"
fi

bin_name="y${year}d${day}${suffix}"
solution_rel="solutions/${year}/day${day}${suffix}.rs"
solution_file="${RUST_DIR}/${solution_rel}"
mkdir -p "$(dirname "${solution_file}")"

if [[ -f "${solution_file}" ]]; then
    echo "Rust solution already exists: ${solution_file}" >&2
else
    cp "${SCRIPT_DIR}/template.rs" "${solution_file}"
    echo "Created ${solution_file}"
fi

bin_rel="src/bin/${bin_name}.rs"
bin_file="${RUST_DIR}/${bin_rel}"
mkdir -p "$(dirname "${bin_file}")"

if [[ ! -f "${bin_file}" ]]; then
    cat <<EOF > "${bin_file}"
use anyhow::Result;
use aoc_rs::runner;

#[path = "../../${solution_rel}"]
mod solution;

fn main() -> Result<()> {
    runner::run(solution::part1, solution::part2)
}
EOF
    echo "Created binary entry ${bin_file}"
fi

mkdir -p "${REPO_ROOT}/input/${year}"
touch "${REPO_ROOT}/input/${year}/day${day}.txt"
touch "${REPO_ROOT}/input/${year}/day${day}_sample.txt"

cargo_toml="${RUST_DIR}/Cargo.toml"
if ! grep -q "name = \"${bin_name}\"" "${cargo_toml}" 2>/dev/null; then
    {
        echo
        echo "[[bin]]"
        echo "name = \"${bin_name}\""
        echo "path = \"${bin_rel}\""
    } >> "${cargo_toml}"
    echo "Registered binary ${bin_name} in Cargo.toml"
fi
