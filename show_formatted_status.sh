#!/bin/bash

# 造轮子调教格式糟糕的status.json
# 2017/06/08, ckj

cat status.json | sed -e 's/^{/{\n\t/'              \
                | sed -e 's/}}$/\n\t}\n}\n/'        \
                | sed -e 's/: {/:\n\t{\n\t\t/g'     \
                | sed -e 's/}, /\n\t},\n\t/g'       \
                | sed -e 's/, /,\n\t\t/g'           \
                | sed -e 's/\t/    /g'
