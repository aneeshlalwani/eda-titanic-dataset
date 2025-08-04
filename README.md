# 🛳 Titanic Dataset Analysis

This project performs **exploratory data analysis (EDA)** and **visualization** on the famous Titanic dataset using **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 📁 Dataset Summary

- **Total Records**: 891 passengers  
- **Features**: 12 columns including:
  - `Survived` (Target)
  - `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare`, `Cabin`, `Embarked`

---

## 🧹 Data Cleaning

- **Missing Values Handled**:
  - `Age`: 177 missing → filled with **median** (due to skewed distribution)
  - `Embarked`: 2 missing → filled with **mode**
  - `Cabin`: Dropped due to >75% missing values

- **Created Features**:
  - `FamilySize = SibSp + Parch`
  - `AgeGroup`: Categorized into `Child`, `Adult`, `Senior`

---

## 📊 Key Exploratory Analysis

### 🎯 Survival Counts
- **Survived**: 342  
- **Did not survive**: 549

---

### 👨‍👩‍👧‍👦 Survival Rate by Gender

| Gender | Survival Rate (%) |
|--------|-------------------|
| Female | 74.2%             |
| Male   | 18.9%             |

---

### 💳 Survival Rate by Ticket Class (Pclass)

| Class | Survival Rate (%) |
|-------|-------------------|
| 1st   | 63.0%             |
| 2nd   | 47.3%             |
| 3rd   | 24.2%             |

---

### 🧓 Age Group Survival Rate

| Age Group | Survival Rate (%) |
|-----------|-------------------|
| Child     | 57.4%             |
| Adult     | 37.1%             |
| Senior    | 26.9%             |

---

### 👨‍👩‍👧‍👦 Survival by Family Size

| Family Size | Survival Rate (%) |
|-------------|-------------------|
| 0 (Alone)   | 30.4%             |
| 1–3         | 55%–72%           |
| 4+          | Drops to 0–20%    |

---

### 💵 Fare and Survival

| Status         | Avg. Fare |
|----------------|-----------|
| Survived       | $48.40    |
| Not Survived   | $22.12    |

> 💡 Higher fare passengers had better survival chances — reflecting class divide and access to lifeboats.

---

## 📈 Visualizations

- ✅ Survival rate by gender (Bar Chart)
- ✅ Age group vs. survival (Bar Chart)
- ✅ Class-based survival rate (Bar Chart)
- ✅ Family size vs. survival (Bar Chart)
- ✅ Average fare comparison by survival (Bar Chart)
- ✅ Gender distribution (Pie Chart)

---

## 📦 Tools & Libraries Used

- Python 3  
- Pandas  
- Matplotlib  
- Seaborn  
- Spyder IDE / Jupyter Notebook (optional)

---

