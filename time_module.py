import time

# ─── 1. Current Time ───────────────────────────────────────────
print(time.time())           # Unix timestamp (seconds since Jan 1, 1970)
print(time.ctime())          # Human-readable: 'Tue Apr 14 10:30:00 2026'

# ─── 2. Structured Time ────────────────────────────────────────
t = time.localtime()         # Local time as a struct
print(t)                     # local time as a struct
print(t.tm_year)             # 2026
print(t.tm_mon)              # Month (1-12)
print(t.tm_mday)             # Day of month
print(t.tm_hour)             # Hour (0-23)
print(t.tm_min)              # Minute
print(t.tm_sec)              # Second

# ─── 3. Formatting Time ────────────────────────────────────────
formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted)             # e.g. '2026-04-14 10:30:00'

# Common format codes:
# %Y = 4-digit year   %m = month   %d = day
# %H = hour (24h)     %M = minute  %S = second
# %I = hour (12h)     %p = AM/PM   %A = weekday name

# ─── 4. Parsing Time String → Struct ───────────────────────────
parsed = time.strptime("2026-04-14", "%Y-%m-%d")
print(parsed.tm_year)        # 2026

# ─── 5. Sleep (Pause Execution) ────────────────────────────────
print("Start")
time.sleep(2)                # Pause for 2 seconds
print("After 2 seconds")

# ─── 6. Measuring Execution Time ───────────────────────────────

start = time.time()          # Save the current timestamp before work starts

# sum()        → adds all numbers together: 0+1+2+...+999999 = 499,999,500,000
# range()      → generates numbers from 0 to 999,999 (1_000_000 is excluded)
# 1_000_000    → same as 1000000, underscore is just for readability
total = sum(range(1_000_000))

end = time.time()            # Save the timestamp after work finishes

# end - start  → how many seconds the work took  e.g. 0.04521938...
# :.4f         → show only 4 decimal places       e.g. 0.0452
print(f"Elapsed: {end - start:.4f} seconds")

# ─── Better way using perf_counter (higher precision) ──────────

start = time.perf_counter()  # High-resolution timer, better for benchmarking

total = sum(range(1_000_000))

end = time.perf_counter()    # Capture time after work finishes

# end - start  → raw elapsed time  e.g. 0.045219384756...
# :.6f         → show 6 decimal places for more precision  e.g. 0.045219
print(f"Elapsed: {end - start:.6f} seconds")

# ─── 7. Converting Between Formats ────────────────────────────
ts    = time.time()                    # float timestamp  e.g. 1744123456.7891234
local = time.localtime(ts)            # timestamp → struct (local)
utc   = time.gmtime(ts)               # timestamp → struct (UTC)
back  = time.mktime(local)            # struct → back to timestamp

# ts:.0f  → remove all decimals, show whole number only  e.g. 1744123457
# back:.0f → same, so both look clean and equal for comparison
print(f"Roundtrip match: {ts:.0f} == {back:.0f}")