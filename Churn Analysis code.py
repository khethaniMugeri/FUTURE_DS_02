
# CUSTOMER RETENTION & CHURN ANALYSIS DASHBOARD
# Telco Customer Churn Dataset
# ----------------------------------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np


# LOADing and preparing data
# ----------------------------------------------------------------------------------------------------------

df = pd.read_csv(r'C:\Anaconda3\Churn Analysis\Telco_Customer_Churn.csv')

# TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# Senior Citizen label
df['Senior_Label'] = df['SeniorCitizen'].map({0: 'Non-Senior', 1: 'Senior'})

# CALCULATE KPIs
#-----------------------------------------------------------------------------------------------------------

total_customers = len(df)
total_churned   = df[df['Churn'] == 'Yes'].shape[0]
churn_rate      = round(total_churned / total_customers * 100, 2)
retention_rate  = round(100 - churn_rate, 2)
total_revenue   = round(df['TotalCharges'].sum(), 2)
churned_revenue = round(df[df['Churn'] == 'Yes']['TotalCharges'].sum(), 2)


# COLOUR THEME
# ------------------------------------------------------------------------------------------------------------

bg_color    = '#E8EEF4'
card_color  = '#FFFFFF'
title_color = '#1A3A5C'
dark_blue   = '#2E6DA4'
light_blue  = '#A8C4E0'
text_color  = '#2C3E50'
label_color = '#5D7A96'


# FIGURE & LAYOUT
# ---------------------------------------------------------------------------------------------------

fig = plt.figure(figsize=(22, 13), facecolor=bg_color)
fig.patch.set_facecolor(bg_color)

# Main Title
fig.text(0.5, 0.97,
         'Customer Retention And Churn Analysis',
         ha='center', va='top',
         fontsize=22, fontweight='bold', color=title_color)

# Grid: 3 rows x 3 cols
gs = gridspec.GridSpec(
    3, 3,
    figure=fig,
    top=0.91, bottom=0.06,
    left=0.04, right=0.98,
    hspace=0.45, wspace=0.3,
    height_ratios=[0.18, 0.41, 0.41]
)


# HELPER FUNCTIONS
# ------------------------------------------------------------------------------------------------

def card(ax):
    ax.set_facecolor(card_color)
    for spine in ax.spines.values():
        spine.set_visible(False)

def style_ax(ax):
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.tick_params(colors=text_color)


# ROW 1 — KPI CARDS 
# --------------------------------------------------------------------------------------------------------

kpi_gs = gridspec.GridSpecFromSubplotSpec(
    1, 6, subplot_spec=gs[0, :], wspace=0.04
)

kpis = [
    ('Total\nCustomers',         f'{total_customers:,}'),
    ('Total Churned\nCustomers', f'{total_churned:,}'),
    ('Churn\nRate',              f'{churn_rate:.2f}%'),
    ('Retention\nRate',          f'{retention_rate:.2f}%'),
    ('Total\nRevenue',           f'${total_revenue:,.2f}'),
    ('Total Churned\nRevenue',   f'${churned_revenue:,.2f}'),
]

for i, (label, value) in enumerate(kpis):
    ax = fig.add_subplot(kpi_gs[i])
    card(ax)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    # Label on TOP
    ax.text(0.5, 0.78, label,
            ha='center', va='center',
            fontsize=8.5, color=label_color)

    # Value BELOW label
    ax.text(0.5, 0.38, value,
            ha='center', va='center',
            fontsize=16, fontweight='bold',
            color=title_color)

    # Bottom border line
    ax.axhline(y=0.06, color=dark_blue,
               linewidth=3, xmin=0.1, xmax=0.9)


# ROW 2 — LEFT: Churn by Payment Method 
# ----------------------------------------------------------------------------------

ax1 = fig.add_subplot(gs[1, 0])
card(ax1)

pay_churn = df[df['Churn'] == 'Yes'].groupby('PaymentMethod').size()
pay_total = df.groupby('PaymentMethod').size()
pay_rate  = (pay_churn / pay_total * 100).round(2).sort_values()

short_labels = {
    'Electronic check'          : 'Electronic check',
    'Mailed check'              : 'Mailed check',
    'Bank transfer (automatic)' : 'Bank transfer (autom.)',
    'Credit card (automatic)'   : 'Credit card (automatic)'
}
pay_rate.index = [short_labels.get(i, i) for i in pay_rate.index]

bars1 = ax1.barh(pay_rate.index, pay_rate.values,
                 color=dark_blue, height=0.5, edgecolor='none')

for bar, val in zip(bars1, pay_rate.values):
    ax1.text(val + 0.3,
             bar.get_y() + bar.get_height()/2,
             f'{val:.2f}%',
             va='center', fontsize=8, color=text_color)

ax1.set_xlabel('Churn Rate', fontsize=8, color=label_color)
ax1.set_ylabel('Payment Method', fontsize=8, color=label_color)
ax1.set_title('Churn by Payment Method', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax1.tick_params(labelsize=7)
ax1.set_xlim(0, pay_rate.max() + 12)
ax1.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x:.2f}%'))
style_ax(ax1)


# ROW 2 — MIDDLE: Churn by Senior Citizen (bar chart ascending)
#------------------------------------------------------------------------------------------------------

ax2 = fig.add_subplot(gs[1, 1])
card(ax2)

senior_churn = df[df['Churn'] == 'Yes'].groupby('Senior_Label').size()
senior_total = df.groupby('Senior_Label').size()
senior_rate  = (senior_churn / senior_total * 100).round(2).sort_values(
    ascending= False)  

bar_colors = [light_blue if v == senior_rate.min()
              else dark_blue for v in senior_rate.values]

bars2 = ax2.bar(senior_rate.index, senior_rate.values,
                color=bar_colors, width=0.4, edgecolor='none')

for bar, val in zip(bars2, senior_rate.values):
    ax2.text(bar.get_x() + bar.get_width()/2,
             val + 0.5,
             f'{val:.2f}%',
             ha='center', va='bottom',
             fontsize=10, fontweight='bold', color=title_color)

ax2.set_ylabel('Churn Rate (%)', fontsize=8, color=label_color)
ax2.set_xlabel('Customer Type', fontsize=8, color=label_color)
ax2.set_title('Churn by Senior Citizen', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax2.tick_params(labelsize=9)
ax2.set_ylim(0, senior_rate.max() + 14)
ax2.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x:.2f}%'))
style_ax(ax2)


# ROW 2 — RIGHT: Churn Rate by Internet Service 
#--------------------------------------------------------------------------------------------

ax3 = fig.add_subplot(gs[1, 2])
card(ax3)

inet_churn = df[df['Churn'] == 'Yes'].groupby('InternetService').size()
inet_total = df.groupby('InternetService').size()
inet_rate  = (inet_churn / inet_total * 100).round(2).sort_values()

bars3 = ax3.barh(inet_rate.index, inet_rate.values,
                 color=dark_blue, height=0.4, edgecolor='none')

for bar, val in zip(bars3, inet_rate.values):
    ax3.text(val + 0.5,
             bar.get_y() + bar.get_height()/2,
             f'{val:.2f}%',
             va='center', fontsize=9,
             fontweight='bold', color=title_color)

ax3.set_xlabel('Churn Rate', fontsize=8, color=label_color)
ax3.set_title('Churn Rate by Internet Service', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax3.tick_params(labelsize=8)
ax3.set_xlim(0, inet_rate.max() + 16)
ax3.xaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x:.2f}%'))
style_ax(ax3)


# ROW 3 — LEFT: Churn Distribution 
#----------------------------------------------------------------------------------------------------

ax4 = fig.add_subplot(gs[2, 0])
card(ax4)

churn_dist  = df['Churn'].value_counts()
churn_pct   = (churn_dist / churn_dist.sum() * 100).round(2)
colors_dist = [light_blue, dark_blue]

wedges4, texts4, autotexts4 = ax4.pie(
    churn_dist.values,
    labels=None,
    autopct=lambda pct: f'{round(pct, 2):.2f}%',
    startangle=90,
    colors=colors_dist,
    pctdistance=0.72,
    wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2)
)

for at in autotexts4:
    at.set_fontsize(9)
    at.set_color('white')
    at.set_fontweight('bold')

ax4.set_title('Churn Distribution', fontsize=11,
              fontweight='bold', color=title_color, pad=8)

legend_dist = [
    mpatches.Patch(color=light_blue,
                   label=f'No  ({churn_dist["No"]:,} | {churn_pct["No"]:.2f}%)'),
    mpatches.Patch(color=dark_blue,
                   label=f'Yes ({churn_dist["Yes"]:,} | {churn_pct["Yes"]:.2f}%)')
]
ax4.legend(handles=legend_dist, loc='lower center',
           bbox_to_anchor=(0.5, -0.14), ncol=1,
           fontsize=8, frameon=False)


# ROW 3 — MIDDLE: Churn by Tenure (line graph)
#---------------------------------------------------------------------------------------------------------

ax5 = fig.add_subplot(gs[2, 1])
card(ax5)

tenure_churn = df[df['Churn'] == 'Yes'].groupby('tenure').size()
tenure_total = df.groupby('tenure').size()
tenure_rate  = (tenure_churn / tenure_total * 100).fillna(0).round(2)

ax5.plot(tenure_rate.index, tenure_rate.values,
         color=dark_blue, linewidth=2, marker=None)

ax5.fill_between(tenure_rate.index, tenure_rate.values,
                 alpha=0.15, color=dark_blue)

ax5.set_xlabel('Tenure (months)', fontsize=8, color=label_color)
ax5.set_ylabel('Churn Rate (%)', fontsize=8, color=label_color)
ax5.set_title('Churn by Tenure', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax5.tick_params(labelsize=7)
ax5.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x:.2f}%'))
style_ax(ax5)

# ROW 3 — RIGHT: Churn by Contract Type (bar chart)
#--------------------------------------------------------------------------------------------------

ax6 = fig.add_subplot(gs[2, 2])
card(ax6)

contract_churn = df[df['Churn'] == 'Yes'].groupby('Contract').size()
contract_total = df.groupby('Contract').size()
contract_rate  = (contract_churn / contract_total * 100).round(2).sort_values(
    ascending=False)

bar_colors6 = [dark_blue, dark_blue, light_blue]

bars6 = ax6.bar(contract_rate.index, contract_rate.values,
                color=bar_colors6, width=0.4, edgecolor='none')

for bar, val in zip(bars6, contract_rate.values):
    ax6.text(bar.get_x() + bar.get_width()/2,
             val + 0.5,
             f'{val:.2f}%',
             ha='center', va='bottom',
             fontsize=10, fontweight='bold', color=title_color)

ax6.set_ylabel('Churn Rate (%)', fontsize=8, color=label_color)
ax6.set_xlabel('Contract Type', fontsize=8, color=label_color)
ax6.set_title('Churn by Contract Type', fontsize=11,
              fontweight='bold', color=title_color, pad=8)
ax6.tick_params(labelsize=8)
ax6.set_ylim(0, contract_rate.max() + 14)
ax6.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, _: f'{x:.2f}%'))
style_ax(ax6)

# SAVE & SHOW
#----------------------------------------------------------------------------------------------------

plt.savefig(
    r'C:\Anaconda3\Churn Analysis\Churn_Dashboard.pdf',
    dpi=150, bbox_inches='tight',
    facecolor=bg_color
)

plt.show()

