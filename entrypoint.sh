#!/bin/bash -l

source env/bin/activate

schemathesis run \
  "${SCHEMA}" \
  --hypothesis-database=:memory: \
  --hypothesis-max-examples="${MAX_EXAMPLES}" \
  --checks="${CHECKS}" \
  ${ARGS} \
