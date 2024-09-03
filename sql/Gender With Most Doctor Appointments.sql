select gender,count(appointmentid) as count_per_gender from [dbo].[medical_appointments]
group by gender
