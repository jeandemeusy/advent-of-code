#!/usr/bin/env bash
set -euo pipefail

# Accept two arguments: -y (year) and -d (day).
# Defaults to current year/day when omitted.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
REPO_ROOT="$(cd "${PYTHON_DIR}/.." && pwd)"

year=$(date +"%Y")
day=$(date +"%d")

while getopts "y:d:" flag; do
    case "${flag}" in
        y) year=${OPTARG} ;;
        d) day=${OPTARG} ;;
    esac
done

day=$(printf "%02d" "${day}")

solutions_dir="${PYTHON_DIR}/py/${year}"
mkdir -p "${solutions_dir}"

target_file="${solutions_dir}/day${day}.py"
if [[ ! -f "${target_file}" ]]; then
    cp "${SCRIPT_DIR}/template.py" "${target_file}"
fi

mkdir -p "${REPO_ROOT}/input/${year}"
touch "${REPO_ROOT}/input/${year}/day${day}.txt"
touch "${REPO_ROOT}/input/${year}/day${day}_sample.txt"
