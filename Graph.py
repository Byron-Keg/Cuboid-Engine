import re
import matplotlib.pyplot as plt

# ==========================================
# LOAD LOG
# ==========================================

with open("log.txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = re.compile(
    r"a=(\d+)/(\d+)\s*\|\s*elapsed=([\d.]+)s\s*\|\s*"
    r"AB hits=(\d+)\s*\|\s*Euler bricks=(\d+)\s*\|\s*"
    r"pruned_mod=(\d+)"
)

a_values = []
elapsed_values = []
ab_hits = []
euler_bricks = []
pruned_mod = []

for m in pattern.finditer(text):
    a_values.append(int(m.group(1)))
    elapsed_values.append(float(m.group(3)))
    ab_hits.append(int(m.group(4)))
    euler_bricks.append(int(m.group(5)))
    pruned_mod.append(int(m.group(6)))

if not a_values:
    print("No data found.")
    exit()

# ==========================================
# SPEED CALCULATION
# ==========================================

speed_x = []
speed_y = []

for i in range(1, len(a_values)):
    da = a_values[i] - a_values[i - 1]
    dt = elapsed_values[i] - elapsed_values[i - 1]

    if dt > 0:
        speed_x.append(a_values[i])
        speed_y.append(da / dt)

# ==========================================
# DASHBOARD
# ==========================================

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle(
    "Cuboid Engine Search Analysis",
    fontsize=16,
)

# Time vs A

axs[0, 0].plot(a_values, elapsed_values, marker="o")
axs[0, 0].set_title("Elapsed Time")
axs[0, 0].set_xlabel("A")
axs[0, 0].set_ylabel("Seconds")
axs[0, 0].grid(True)

# AB Hits

axs[0, 1].plot(a_values, ab_hits, marker="o")
axs[0, 1].set_title("AB Hits")
axs[0, 1].set_xlabel("A")
axs[0, 1].set_ylabel("Hits")
axs[0, 1].grid(True)

# Euler Bricks

axs[1, 0].bar(a_values, euler_bricks)
axs[1, 0].set_title("Euler Bricks")
axs[1, 0].set_xlabel("A")
axs[1, 0].set_ylabel("Bricks")

# Search Speed

axs[1, 1].plot(speed_x, speed_y, marker="o")
axs[1, 1].set_title("Search Speed")
axs[1, 1].set_xlabel("A")
axs[1, 1].set_ylabel("A per Second")
axs[1, 1].grid(True)

plt.tight_layout()

plt.savefig("cuboid_dashboard.png", dpi=300)

plt.show()