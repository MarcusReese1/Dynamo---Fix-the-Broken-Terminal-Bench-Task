import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

with open("/app/access.log", encoding="utf-8") as log_file:
    for line in log_file:
        line = line.strip()
        if not line:
            continue

        total += 1
        ips.add(line.split()[0])

        match = re.search(
            r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ',
            line,
        )
        if match:
            paths[match.group(1)] += 1

with open("/app/report.json", "w", encoding="utf-8") as report_file:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": paths.most_common(1)[0][0],
        },
        report_file,
    )