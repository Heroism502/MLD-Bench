import matplotlib.pyplot as plt
import numpy as np

# Set all text to Times New Roman and bold
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['figure.titleweight'] = 'bold'

# Data
categories = [
    "Zebra Crossing", "Diverging Marking", "Low Light", "Arrow",
    "No-stopping", "Strong Light", "Shadow", "Normal",
    "Dedicated Lane", "Turn", "No Line"
]
counts = [467, 609, 1178, 492, 413, 155, 3039, 8649, 140, 136, 1159]
total = 16437

# Create a color palette
colors = plt.cm.tab20(np.linspace(0, 1, len(categories)))

# Create figure with grid background
plt.figure(figsize=(12, 6))
ax = plt.gca()
ax.set_facecolor('#f0f0f0')  # Light gray background
ax.grid(color='white', linestyle='-', linewidth=1)  # White grid lines

# Create bars
bars = plt.bar(categories, counts, color=colors, edgecolor='black', linewidth=0.7)

# Add percentage labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height/total*100:.1f}%',
            ha='center', va='bottom',
            fontsize=14, fontweight='bold')

# Set chart title and labels
# plt.title('Distribution of Road Markings and Conditions', fontsize=16, pad=20)
plt.xlabel('Categories', fontsize=18, labelpad=10)
plt.ylabel('Counts', fontsize=18, labelpad=10)
plt.xticks(rotation=45, ha='right', fontsize=14)
plt.yticks(fontsize=14)

# Add minor grid lines for better readability
ax.grid(which='minor', color='white', linestyle=':', linewidth=0.5)
ax.set_axisbelow(True)  # Ensure grid is behind bars

# Adjust layout
plt.tight_layout()

# Show chart
plt.show()