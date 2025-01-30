# What´s a normal distribution and what´s a non-normal distribution  

1. **A normal distribution (Gaussian distribution)**  
   - This is a **bell-shaped curve** where most values are **centered around the mean**, and fewer values appear at the extremes.  
   - Example: Heights of people, IQ scores, or standardized test scores.  

2. **A non-normal distribution**  
   - This could be **skewed (left or right)**, **uniform**, or **bimodal**.  
   - Example: Income distribution (which is often **right-skewed**, meaning most people earn a low-to-moderate amount, but a few people earn very high salaries).  

I'll generate and plot both distributions for you. 🚀

Here’s the visualization of both distributions:

1. **Left Plot (Normal Distribution)**:  
   - This is a **bell-shaped curve** where most values are around the mean (~50).  
   - The values **symmetrically** decrease as they move away from the center.  
   - Example: Heights, IQ scores, or standardized test scores.

2. **Right Plot (Non-Normal Distribution - Right-Skewed)**:  
   - Most values are **clustered on the left**, but a few extreme values stretch far to the right.  
   - This is common in **income distribution**, where most people earn a low-to-moderate amount, but a few earn much more.  

### **Why This Matters?**
- **StandardScaler (Z-score normalization)** works best with **normal distributions**.
- **MinMaxScaler (Min-max normalization)** is better when **data is not normally distributed** (e.g., right-skewed data like salaries).
