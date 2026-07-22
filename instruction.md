Analyze the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

Success criteria:

1. `/app/report.json` is a valid JSON object containing exactly the keys `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the number of non-empty log entries and `unique_ips` is the number of distinct client IP addresses.
3. `top_path` is the request path that occurs most often in the log.