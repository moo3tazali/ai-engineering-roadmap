companies = [
    {
        "name": "MESCo",
        "country": "Egypt",
        "departments": ["IT", "Finance", "Procurement"],
    },
    {
        "name": "SACO",
        "country": "Saudi Arabia",
        "departments": ["Operations", "Commercial"],
    },
]

print(companies[1]["name"])
print(companies[0]["departments"][2])
companies[0]["departments"].append("HR")
companies[1]["country"] = "KSA"
companies[0]["active"] = True
print(companies)
for company in companies:
    print(f"{company['name']} - {company['country']}")
