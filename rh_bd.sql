CREATE DATABASE IF NOT EXISTS hr_analytics_db;
USE hr_analytics_db;

-- 1. TABLA: EMPLEADOS 
CREATE TABLE IF NOT EXISTS empleados (
    EmployeeNumber INT PRIMARY KEY,
    Age INT,
    Gender VARCHAR(20),
    MaritalStatus VARCHAR(20),
    Education INT,
    EducationField VARCHAR(100),
    DistanceFromHome INT,
    Attrition VARCHAR(5) -- Nuestra variable objetivo
);

-- 2. TABLA: PUESTOS 
CREATE TABLE IF NOT EXISTS puestos_trabajo (
    EmployeeNumber INT PRIMARY KEY,
    Department VARCHAR(100),
    JobRole VARCHAR(100),
    JobLevel INT,
    MonthlyIncome DECIMAL(10,2),
    OverTime VARCHAR(5),
    BusinessTravel VARCHAR(50),
    StockOptionLevel INT,
    FOREIGN KEY (EmployeeNumber) REFERENCES empleados(EmployeeNumber)
);

-- 3. TABLA: RANKING_SATISFACCION (Todos los indicadores juntos)
CREATE TABLE IF NOT EXISTS ranking_satisfaccion (
    EmployeeNumber INT PRIMARY KEY,
    EnvironmentSatisfaction INT,
    JobSatisfaction INT,
    RelationshipSatisfaction INT,
    WorkLifeBalance INT,
    JobInvolvement INT,
    PerformanceRating INT,
    FOREIGN KEY (EmployeeNumber) REFERENCES empleados(EmployeeNumber)
);

-- 4. TABLA: HISTORIAL_LABORAL 
CREATE TABLE IF NOT EXISTS historial_laboral (
    EmployeeNumber INT PRIMARY KEY,
    TotalWorkingYears INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT,
    NumCompaniesWorked INT,
    PercentSalaryHike INT,
    FOREIGN KEY (EmployeeNumber) REFERENCES empleados(EmployeeNumber)
);