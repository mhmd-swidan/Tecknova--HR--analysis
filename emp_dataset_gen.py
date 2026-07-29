import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# عدد الموظفين
n_employees = 1000

# -----------------------------
# Lists / Categories
# -----------------------------

departments = {
    "Engineering": [
        "Software Engineer",
        "Data Engineer",
        "Backend Developer",
        "Frontend Developer",
        "Engineering Manager"
    ],
    "IT": [
        "System Administrator",
        "Network Engineer",
        "IT Support Specialist",
        "IT Manager"
    ],
    "Sales": [
        "Sales Representative",
        "Account Executive",
        "Sales Manager"
    ],
    "Customer Service": [
        "Customer Support Specialist",
        "Customer Success Manager"
    ],
    "Marketing": [
        "Marketing Specialist",
        "SEO Specialist",
        "Marketing Manager"
    ],
    "Finance": [
        "Accountant",
        "Financial Analyst",
        "Finance Manager"
    ],
    "HR": [
        "HR Specialist",
        "Recruiter",
        "HR Manager"
    ],
    "Operations": [
        "Operations Specialist",
        "Operations Manager"
    ],
    "Legal": [
        "Legal Advisor",
        "Legal Specialist"
    ],
    "Administration": [
        "Administrative Assistant",
        "Office Manager"
    ]
}


department_distribution = {
    "Engineering": 300,
    "IT": 150,
    "Sales": 120,
    "Customer Service": 100,
    "Marketing": 80,
    "Finance": 70,
    "HR": 50,
    "Operations": 50,
    "Legal": 30,
    "Administration": 50
}


education_levels = [
    "Diploma",
    "Bachelor",
    "Master",
    "PhD"
]

education_weights = [
    0.10,
    0.65,
    0.22,
    0.03
]


job_levels = [
    "Entry Level",
    "Mid Level",
    "Senior",
    "Lead",
    "Manager"
]

job_level_weights = [
    0.25,
    0.40,
    0.22,
    0.08,
    0.05
]


employment_types = [
    "Full-Time",
    "Part-Time",
    "Contract"
]

employment_weights = [
    0.85,
    0.10,
    0.05
]


locations = [
    "Riyadh",
    "Jeddah",
    "Dubai",
    "Cairo",
    "London"
]


marital_status = [
    "Single",
    "Married",
    "Divorced"
]
job_structure = {

    "Engineering": {
        "Entry Level": [
            "Junior Software Engineer",
            "Junior Backend Developer",
            "Junior Frontend Developer",
            "Junior Data Engineer"
        ],
        "Mid Level": [
            "Software Engineer",
            "Backend Developer",
            "Frontend Developer",
            "Data Engineer"
        ],
        "Senior": [
            "Senior Software Engineer",
            "Senior Backend Developer",
            "Senior Frontend Developer",
            "Senior Data Engineer"
        ],
        "Lead": [
            "Tech Lead",
            "Engineering Lead"
        ],
        "Manager": [
            "Engineering Manager"
        ]
    },

    "IT": {
        "Entry Level": [
            "Junior IT Support",
            "Junior System Administrator",
            "Junior Network Engineer"
        ],
        "Mid Level": [
            "IT Support Specialist",
            "System Administrator",
            "Network Engineer"
        ],
        "Senior": [
            "Senior IT Support Specialist",
            "Senior System Administrator",
            "Senior Network Engineer"
        ],
        "Lead": [
            "IT Team Lead"
        ],
        "Manager": [
            "IT Manager"
        ]
    },

    "Sales": {
        "Entry Level": [
            "Junior Sales Representative"
        ],
        "Mid Level": [
            "Sales Representative",
            "Account Executive"
        ],
        "Senior": [
            "Senior Account Executive",
            "Senior Sales Representative"
        ],
        "Lead": [
            "Sales Team Lead"
        ],
        "Manager": [
            "Sales Manager"
        ]
    },

    "Customer Service": {
        "Entry Level": [
            "Junior Customer Support"
        ],
        "Mid Level": [
            "Customer Support Specialist",
            "Customer Success Specialist"
        ],
        "Senior": [
            "Senior Customer Support Specialist",
            "Senior Customer Success Specialist"
        ],
        "Lead": [
            "Customer Support Lead"
        ],
        "Manager": [
            "Customer Service Manager"
        ]
    },

    "Marketing": {
        "Entry Level": [
            "Junior Marketing Specialist",
            "Junior SEO Specialist"
        ],
        "Mid Level": [
            "Marketing Specialist",
            "SEO Specialist",
            "Content Specialist"
        ],
        "Senior": [
            "Senior Marketing Specialist",
            "Senior SEO Specialist"
        ],
        "Lead": [
            "Marketing Lead"
        ],
        "Manager": [
            "Marketing Manager"
        ]
    },

    "Finance": {
        "Entry Level": [
            "Junior Accountant"
        ],
        "Mid Level": [
            "Accountant",
            "Financial Analyst"
        ],
        "Senior": [
            "Senior Accountant",
            "Senior Financial Analyst"
        ],
        "Lead": [
            "Finance Lead"
        ],
        "Manager": [
            "Finance Manager"
        ]
    },

    "HR": {
        "Entry Level": [
            "Junior HR Specialist"
        ],
        "Mid Level": [
            "HR Specialist",
            "Recruiter"
        ],
        "Senior": [
            "Senior HR Specialist",
            "Senior Recruiter"
        ],
        "Lead": [
            "HR Lead"
        ],
        "Manager": [
            "HR Manager"
        ]
    },

    "Operations": {
        "Entry Level": [
            "Junior Operations Specialist"
        ],
        "Mid Level": [
            "Operations Specialist"
        ],
        "Senior": [
            "Senior Operations Specialist"
        ],
        "Lead": [
            "Operations Lead"
        ],
        "Manager": [
            "Operations Manager"
        ]
    },

    "Legal": {
        "Entry Level": [
            "Junior Legal Advisor"
        ],
        "Mid Level": [
            "Legal Advisor"
        ],
        "Senior": [
            "Senior Legal Advisor"
        ],
        "Lead": [
            "Legal Lead"
        ],
        "Manager": [
            "Legal Manager"
        ]
    },

    "Administration": {
        "Entry Level": [
            "Administrative Assistant"
        ],
        "Mid Level": [
            "Office Administrator"
        ],
        "Senior": [
            "Senior Office Administrator"
        ],
        "Lead": [
            "Administration Lead"
        ],
        "Manager": [
            "Administration Manager"
        ]
    }

}
# -----------------------------
# Job Level Rules
# -----------------------------

job_level_rules = {
    "Entry Level": (0, 2),
    "Mid Level": (3, 7),
    "Senior": (8, 12),
    "Lead": (13, 18),
    "Manager": (19, 25)
}


# -----------------------------
# Function to determine Job Level
# -----------------------------

def get_job_level(years_experience):

    for level, (min_exp, max_exp) in job_level_rules.items():

        if min_exp <= years_experience <= max_exp:
            return level

    return "Entry Level"
# -----------------------------
# Generate Employees
# -----------------------------

employees = []

employee_ids = [
    f"EMP{i:04d}" 
    for i in range(1, n_employees + 1)
]


# Create department list according to distribution
department_list = []

for dept, count in department_distribution.items():
    department_list.extend([dept] * count)

random.shuffle(department_list)


for i in range(n_employees):

    dept = department_list[i]

    hire_date = fake.date_between(
        start_date="-15y",
        end_date="today"
    )

    birth_date = fake.date_between(
        start_date="-60y",
        end_date="-22y"
    )


    years_experience = random.randint(
        0,
        min(
            25,
            datetime.today().year - birth_date.year - 18
        )
    )
        # Calculate Job Level
    job_level = get_job_level(years_experience)

    # Select Job Title based on Department and Job Level
    job_title = random.choice(
        job_structure[dept][job_level]
    )

    employees.append({

        "employee_id": employee_ids[i],

        "first_name": fake.first_name(),

        "last_name": fake.last_name(),

        "gender": random.choices(
            ["Male", "Female"],
            weights=[0.6, 0.4]
        )[0],

        "date_of_birth": birth_date,

        "hire_date": hire_date,

        "department": dept,

        "job_title": job_title,

        "job_level": job_level,

        "employment_type": random.choices(
            employment_types,
            weights=employment_weights
        )[0],

        "education_level": random.choices(
            education_levels,
            weights=education_weights
        )[0],

        "marital_status": random.choice(
            marital_status
        ),

        "location": random.choice(
            locations
        ),

        "years_experience": years_experience,

        "manager_id": None
    })


employees_df = pd.DataFrame(employees)

print("  employee finished ")
employees_df.head()
# ------------------------------------------
# Ensure every department has at least one Manager
# ------------------------------------------

for dept in employees_df["department"].unique():

    managers = employees_df[
        (employees_df["department"] == dept) &
        (employees_df["job_level"] == "Manager")
    ]

    if len(managers) == 0:

        dept_employees = employees_df[
            employees_df["department"] == dept
        ]

        most_experienced = dept_employees[
            "years_experience"
        ].idxmax()

        employees_df.loc[
            most_experienced,
            "job_level"
        ] = "Manager"

        employees_df.loc[
            most_experienced,
            "job_title"
        ] = random.choice(
            job_structure[dept]["Manager"]
        )


# # ------------------------------------------
# # Create manager_id column
# # ------------------------------------------

# employees_df["manager_id"] = None


# # ------------------------------------------
# # Assign Manager for each employee
# # ------------------------------------------

# for dept in employees_df["department"].unique():

#     dept_employees = employees_df[
#         employees_df["department"] == dept
#     ]

#     managers = dept_employees[
#         dept_employees["job_level"] == "Manager"
#     ]

#     manager_ids = managers["employee_id"].tolist()

#     for index, row in dept_employees.iterrows():

#         # Managers don't report to anyone
#         if row["job_level"] == "Manager":
#             continue

#         employees_df.loc[
#             index,
#             "manager_id"
#         ] = random.choice(manager_ids)

# ------------------------------------------
# create salary table
# ------------------------------------------

# ------------------------------------------
# Salary Ranges by Job Level
# ------------------------------------------

salary_ranges = {

    "Entry Level": (3000, 6000),

    "Mid Level": (6000, 10000),

    "Senior": (10000, 16000),

    "Lead": (16000, 22000),

    "Manager": (22000, 35000)

}


# ------------------------------------------
# Create Salary Records
# ------------------------------------------

salary_records = []

salary_counter = 1


for _, employee in employees_df.iterrows():

    employee_id = employee["employee_id"]

    job_level = employee["job_level"]

    hire_date = employee["hire_date"]


    # Number of salary changes
    num_records = random.randint(1, 3)


    # Get salary range
    min_salary, max_salary = salary_ranges[job_level]


    # Initial salary
    current_salary = random.randint(
        min_salary,
        max_salary
    )


    salary_date = hire_date


    # Create salary history
    for record in range(num_records):


        # First record has no increment
        if record == 0:

            increment_percentage = 0


        else:

            increment_percentage = random.randint(
                3,
                10
            )


            current_salary = current_salary * (
                1 + increment_percentage / 100
            )


            # Increase date by 1-2 years
            salary_date = salary_date + pd.DateOffset(
                years=random.randint(1, 2)
            )


        # Bonus
        bonus = random.randint(
            0,
            int(current_salary * 0.15)
        )


        # Total compensation
        total_salary = current_salary + bonus


        # Salary ID
        salary_id = f"SAL{salary_counter:05d}"


        salary_records.append({

            "salary_id": salary_id,

            "employee_id": employee_id,

            "salary_date": salary_date,

            "base_salary": round(current_salary, 2),

            "bonus": bonus,

            "increment_percentage": increment_percentage,

            "total_salary": round(total_salary, 2)

        })


        salary_counter += 1



# Convert to DataFrame

salary_df = pd.DataFrame(salary_records)
print("  salary finished ")

# ------------------------------------------
# Performance Levels
# ------------------------------------------

performance_levels = {

    1: "Poor",

    2: "Needs Improvement",

    3: "Meets Expectations",

    4: "Exceeds Expectations",

    5: "Outstanding"

}


# ------------------------------------------
# Reviewers
# ------------------------------------------

reviewers = [

    "HR Department",

    "Department Manager",

    "Team Lead"

]


# ------------------------------------------
# Create Performance Reviews
# ------------------------------------------

performance_reviews = []

review_counter = 1


for _, employee in employees_df.iterrows():

    employee_id = employee["employee_id"]

    hire_date = employee["hire_date"]


    # Number of reviews per employee
    num_reviews = random.randint(2, 4)


    for review in range(num_reviews):


        # Weighted rating
        rating = random.choices(

            [1, 2, 3, 4, 5],

            weights=[0.05, 0.10, 0.35, 0.35, 0.15]

        )[0]


        # KPI score based on rating

        if rating == 1:

            kpi_score = random.randint(40, 59)


        elif rating == 2:

            kpi_score = random.randint(60, 69)


        elif rating == 3:

            kpi_score = random.randint(70, 79)


        elif rating == 4:

            kpi_score = random.randint(80, 89)


        else:

            kpi_score = random.randint(90, 100)



        performance_reviews.append({

            "review_id": f"REV{review_counter:05d}",

            "employee_id": employee_id,

            "review_date": hire_date + pd.DateOffset(
                years=review + 1
            ),

            "rating": rating,

            "kpi_score": kpi_score,

            "performance_level": performance_levels[rating],

            "reviewer": random.choice(reviewers),

            "comments": fake.sentence()

        })


        review_counter += 1



# ------------------------------------------
# Convert to DataFrame
# ------------------------------------------

performance_df = pd.DataFrame(performance_reviews)

print("  performance finished ")
# ------------------------------------------
# Attrition Reasons
# ------------------------------------------

attrition_reasons = [

    "Better Opportunity",

    "Salary Issues",

    "Career Change",

    "Relocation",

    "Personal Reasons",

    "Performance"

]


# ------------------------------------------
# Exit Types
# ------------------------------------------

exit_types = [

    "Resigned",

    "Terminated",

    "Retired"

]


# ------------------------------------------
# Create Attrition Records
# ------------------------------------------

attrition_records = []

attrition_counter = 1


# Select employees who left the company

num_attrition = random.randint(150, 250)


attrition_employees = employees_df.sample(
    n=num_attrition,
    random_state=42
)



# Generate attrition data

for _, employee in attrition_employees.iterrows():

    employee_id = employee["employee_id"]

    hire_date = employee["hire_date"]


    # Exit date after hire date

    exit_date = fake.date_between(
        start_date=hire_date,
        end_date="today"
    )


    # Years worked in company

    years_at_company = (
        exit_date.year -
        hire_date.year
    )


    attrition_records.append({

        "attrition_id": f"ATT{attrition_counter:05d}",

        "employee_id": employee_id,

        "exit_date": exit_date,

        "reason": random.choice(
            attrition_reasons
        ),

        "exit_type": random.choice(
            exit_types
        ),

        "years_at_company": years_at_company

    })


    attrition_counter += 1



# ------------------------------------------
# Convert to DataFrame
# ------------------------------------------

attrition_df = pd.DataFrame(attrition_records)
print("  attrition finished ")

employees_df.to_csv("employees.csv",index=False)
salary_df.to_csv("salary.csv",index=False)
performance_df.to_csv("employee_performance.csv",index=False)
attrition_df.to_csv("employees_attrition.csv",index=False)
print("finished")