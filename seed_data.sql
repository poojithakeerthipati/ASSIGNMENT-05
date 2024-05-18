INSERT INTO Venue
    (Venue_id, Venue_name, address)
VALUES
    ('V001', 'City Cinema', '123 Main St'),
    ('V002', 'Stadium Arena', '456 Stadium Ave'),
    ('V003', 'Music Hall', '789 Center Blvd'),
    ('V004', 'Town Hall', '101 Oak St'),
    ('V005', 'Sports Center', '555 Arena Rd'),
    ('V006', 'Lakefront Pavilion', '888 Lakeview Dr'),
    ('V007', 'Theater District', '333 Broadway'),
    ('V008', 'Garden Amphitheater', '444 Park Ave'),
    ('V009', 'Community Center', '777 Elm St'),
    ('V010', 'Event Hall', '222 Center Ave');

-- Inserting sample records into EVENT table
INSERT INTO EVENT
    (EVENT_ID, EVENT_NAME, EVENT_DATE, EVENT_TIME, VENUE_ID, TOTAL_SEATS, AVAILABLE_SEATS, TICKET_PRICE, EVENT_TYPE)
VALUES
    ('E001', 'Avengers: Endgame', '2024-05-15', '19:00:00', 'V001', 200, 200, 12.50, 'Movie'),
    ('E002', 'NBA Finals Game 1', '2024-06-10', '20:00:00', 'V002', 18000, 18000, 75.00, 'Sports'),
    ('E003', 'Taylor Swift Live', '2024-07-05', '21:00:00', 'V003', 5000, 5000, 100.00, 'Concert'),
    ('E004', 'Local Comedy Night', '2024-06-25', '19:30:00', 'V007', 150, 150, 20.00, 'Other'),
    ('E005', 'Family Movie Day', '2024-05-20', '14:00:00', 'V010', 100, 100, 8.00, 'Movie'),
    ('E006', 'High School Graduation', '2024-06-15', '15:00:00', 'V004', 500, 500, 0.00, 'Other'),
    ('E007', 'Summer Music Festival', '2024-07-20', '16:00:00', 'V006', 3000, 3000, 50.00, 'Concert'),
    ('E008', 'Charity Gala', '2024-08-05', '18:30:00', 'V008', 400, 400, 150.00, 'Other'),
    ('E009', 'Soccer Match', '2024-06-01', '19:45:00', 'V005', 15000, 15000, 30.00, 'Sports'),
    ('E010', 'Classic Movie Night', '2024-05-30', '19:00:00', 'V001', 150, 150, 10.00, 'Movie');

-- Inserting sample records into CUSTOMER table
INSERT INTO CUSTOMER
    (CUSTOMER_ID, CUSTOMER_NAME, EMAIL, PHONE_NUMBER)
VALUES
    ('C001', 'Alice Johnson', 'alice@example.com', '123-456-7890'),
    ('C002', 'Bob Smith', 'bob@example.com', '987-654-3210'),
    ('C003', 'Carol Davis', 'carol@example.com', '555-123-4567'),
    ('C004', 'David Lee', 'david@example.com', '333-555-7777'),
    ('C005', 'Emily White', 'emily@example.com', '999-888-7777'),
    ('C006', 'Frank Brown', 'frank@example.com', '444-222-1111'),
    ('C007', 'Grace Taylor', 'grace@example.com', '777-999-1111'),
    ('C008', 'Henry Clark', 'henry@example.com', '111-333-5555'),
    ('C009', 'Ivy Anderson', 'ivy@example.com', '222-444-6666'),
    ('C010', 'Jack Roberts', 'jack@example.com', '666-888-2222');

-- Inserting sample records into BOOKING table with manually generated BOOKING_ID values
INSERT INTO BOOKING
    (BOOKING_ID, CUSTOMER_ID, EVENT_ID, NUM_TICKETS, TOTAL_COST, BOOKING_DATE)
VALUES
    ('B001', 'C001', 'E001', 2, 25.00, '2024-05-10'),
    ('B002', 'C002', 'E002', 4, 300.00, '2024-06-01'),
    ('B003', 'C003', 'E003', 3, 300.00, '2024-07-01'),
    ('B004', 'C004', 'E004', 1, 20.00, '2024-06-20'),
    ('B005', 'C005', 'E005', 5, 40.00, '2024-05-15'),
    ('B006', 'C006', 'E006', 10, 0.00, '2024-06-05'),
    ('B007', 'C007', 'E007', 2, 100.00, '2024-07-10'),
    ('B008', 'C008', 'E008', 2, 300.00, '2024-08-01'),
    ('B009', 'C009', 'E009', 3, 90.00, '2024-05-25'),
    ('B010', 'C010', 'E010', 2, 20.00, '2024-05-20');

USE TICKET_BOOKING_SYSTEM;
--Write a SQL query to list all Events.

SELECT *
FROM EVENT;
seLECT *
FROM BOOKING;
SELECT *
FROM CUSTOMER;
SELECT *
FROM VENUE;