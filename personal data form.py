# Personal Input Form Program

def personal_input_form():
    print("=== Personal Input Form ===\n")

    # Section 1: Basic Information
    name = input("Full Name: ")
    dob = input("Date of Birth (DD/MM/YYYY): ")
    gender = input("Gender: (Male/Female)")
    nationality = input("Nationality: ")
    phone = input("Contact Number: ")
    email = input("Email Address: ")
    address = input("Address: ")

    # Section 2: Identification
    id_number = input("ID/Passport Number: ")
    marital_status = input("Marital Status: ")

    # Section 3: Education
    qualification = input("Highest Qualification: ")
    institution = input("Institution Name: ")
    year_of_passing = input("Year of Passing: ")
    specialization = input("Specialization: ")

    # Section 4: Professional
    occupation = input("Current Occupation: ")
    company = input("Company/Organization: ")
    experience = input("Work Experience (Years): ")
    skills = input("Skills/Expertise: ")

    # Section 5: Emergency Contact
    emergency_name = input("Emergency Contact Name: ")
    emergency_relation = input("Relationship: ")
    emergency_phone = input("Emergency Contact Number: ")

    # Section 6: Preferences
    languages = input("Languages Known: ")
    hobbies = input("Hobbies/Interests: ")
    requirements = input("Special Requirements (medical/dietary/accessibility): ")

    # Section 7: Declaration
    signature = input("Signature: ")
    date = input("Date (DD/MM/YYYY): ")

    # Display collected information
    print("\n=== Form Submitted Successfully ===")
    print(f"Name: {name}")
    print(f"DOB: {dob}")
    print(f"Gender: {gender}")
    print(f"Nationality: {nationality}")
    print(f"Phone: {phone}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"ID Number: {id_number}")
    print(f"Marital Status: {marital_status}")
    print(f"Qualification: {qualification}")
    print(f"Institution: {institution}")
    print(f"Year of Passing: {year_of_passing}")
    print(f"Specialization: {specialization}")
    print(f"Occupation: {occupation}")
    print(f"Company: {company}")
    print(f"Experience: {experience}")
    print(f"Skills: {skills}")
    print(f"Emergency Contact: {emergency_name} ({emergency_relation}) - {emergency_phone}")
    print(f"Languages Known: {languages}")
    print(f"Hobbies: {hobbies}")
    print(f"Special Requirements: {requirements}")
    print(f"Signature: {signature}")
    print(f"Date: {date}")

# Run the form
if __name__ == "__main__":
    personal_input_form()
