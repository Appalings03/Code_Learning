-- Keep a log of any SQL queries you execute as you solve the mystery.
CREATE TABLE crime_scene_reports (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    street TEXT,
    description TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE interviews (
    id INTEGER,
    name TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    transcript TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE atm_transactions (
    id INTEGER,
    account_number INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    atm_location TEXT,
    transaction_type TEXT,
    amount INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE bank_accounts (
    account_number INTEGER,
    person_id INTEGER,
    creation_year INTEGER,
    FOREIGN KEY(person_id) REFERENCES people(id)
);
CREATE TABLE airports (
    id INTEGER,
    abbreviation TEXT,
    full_name TEXT,
    city TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE flights (
    id INTEGER,
    origin_airport_id INTEGER,
    destination_airport_id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    PRIMARY KEY(id),
    FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
    FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
);
CREATE TABLE passengers (
    flight_id INTEGER,
    passport_number INTEGER,
    seat TEXT,
    FOREIGN KEY(flight_id) REFERENCES flights(id)
);
CREATE TABLE phone_calls (
    id INTEGER,
    caller TEXT,
    receiver TEXT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    duration INTEGER,
    PRIMARY KEY(id)
);
CREATE TABLE people (
    id INTEGER,
    name TEXT,
    phone_number TEXT,
    passport_number INTEGER,
    license_plate TEXT,
    PRIMARY KEY(id)
);
CREATE TABLE bakery_security_logs (
    id INTEGER,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    hour INTEGER,
    minute INTEGER,
    activity TEXT,
    license_plate TEXT,
    PRIMARY KEY(id)
);
--.schema just to see what kind of info are stored
SELECT * FROM crime_scene_reports;
SELECT id, description FROM crime_scene_reports WHERE (year = 2024 AND day = 28 AND month = 7)
-- Get 5 crime
--+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
--| id  |                                                                                                       description                                                                                                        |
--+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
--| 293 | Vandalism took place at 12:04. No known witnesses.                                                                                                                                                                       |
--| 294 | Shoplifting took place at 03:01. Two people witnessed the event.                                                                                                                                                         |
--| 295 | Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
--| 296 | Money laundering took place at 20:30. No known witnesses.                                                                                                                                                                |
--| 297 | Littering took place at 16:36. No known witnesses.                                                                                                                                                                       |
--+-----+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

--295 THEFT OF DUCK; 10:15am; 3 WITNESSES -> mentions bakery

--CHECK WITNESS testimony
SELECT id, name, transcript FROM interviews WHERE day = 28 AND month = 7 AND year = 2024;
--+-----+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
--| 158 | Jose    | “Ah,” said he, “I forgot that I had not seen you for some weeks. It is a little souvenir from the King of Bohemia in return for my assistance in the case of the Irene Adler papers.”                                                                                                                               |
--| 159 | Eugene  | “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”                                                                                                                                                                                      |
--| 160 | Barbara | “You had my note?” he asked with a deep harsh voice and a strongly marked German accent. “I told you that I would call.” He looked from one to the other of us, as if uncertain which to address.                                                                                                                   |
--| 161 | Ruth    | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
--| 162 | Eugene  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
--| 163 | Raymond | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |
--| 191 | Lily    | Our neighboring courthouse has a very annoying rooster that crows loudly at 6am every day. My sons Robert and Patrick took the rooster to a city far, far away, so it may never bother us again. My sons have successfully arrived in Paris.                                                                        |
--+-----+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
-- 161 Ruth
-- 162 Eugene
-- 163 Raymond

.schema bakery_security_logs
-- look at what kind of info are store

SELECT id, activity, license_plate FROM bakery_security_logs WHERE year=2024 AND month=7 AND day=28 AND hour=10 AND minute BETWEEN 10 AND 30;

--+-----+----------+---------------+
--| id  | activity | license_plate |
--+-----+----------+---------------+
--| 259 | entrance | 13FNH73       |
--| 260 | exit     | 5P2BI95       |
--| 261 | exit     | 94KL13X       |
--| 262 | exit     | 6P58WS2       |
--| 263 | exit     | 4328GD8       |
--| 264 | exit     | G412CB7       |
--| 265 | exit     | L93JTIZ       |
--| 266 | exit     | 322W7JE       |
--| 267 | exit     | 0NTHK55       |
--+-----+----------+---------------+

--link license_plate with name and other info
SELECT * FROM people WHERE license_plate IN (
  SELECT license_plate FROM bakery_security_logs
  WHERE year=2024 AND month=7 AND day=28 AND hour=10 AND minute BETWEEN 10 AND 30
);

--+--------+---------+----------------+-----------------+---------------+
--|   id   |  name   |  phone_number  | passport_number | license_plate |
--+--------+---------+----------------+-----------------+---------------+
--| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
--| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
--| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
--| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
--| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
--| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
--| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
--| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
--| 745650 | Sophia  | (027) 555-1068 | 3642612721      | 13FNH73       |
--+--------+---------+----------------+-----------------+---------------+
-- check for transaction from those people
SELECT id, account_number, atm_location, transaction_type, amount FROM atm_transactions
WHERE year=2024 AND month=7 AND day=28 AND account_number IN (
  SELECT account_number FROM bank_accounts WHERE person_id IN (
    SELECT id FROM people WHERE license_plate IN (
      SELECT license_plate FROM bakery_security_logs
      WHERE year=2024 AND month=7 AND day=28 AND hour=10 AND minute BETWEEN 0 AND 30
    )
  )
);

--+-----+----------------+----------------------+------------------+--------+
--| id  | account_number |     atm_location     | transaction_type | amount |
--+-----+----------------+----------------------+------------------+--------+
--| 246 | 28500762       | Leggett Street       | withdraw         | 48     |
--| 267 | 49610011       | Leggett Street       | withdraw         | 50     |
--| 288 | 25506511       | Leggett Street       | withdraw         | 20     |
--| 292 | 56171033       | Daboin Sanchez Drive | deposit          | 70     |
--| 336 | 26013199       | Leggett Street       | withdraw         | 35     |
--| 340 | 86850293       | Blumberg Boulevard   | deposit          | 60     |
--+-----+----------------+----------------------+------------------+--------+

--Look for flight booked after the crime know with the interview

SELECT id, origin_airport_id, destination_airport_id,hour, minute FROM flights
WHERE year=2024 AND month=7 AND day=29
ORDER BY hour, minute
LIMIT 10;

--+----+-------------------+------------------------+------+--------+
--| id | origin_airport_id | destination_airport_id | hour | minute |
--+----+-------------------+------------------------+------+--------+
--| 36 | 8                 | 4                      | 8    | 20     |
--| 43 | 8                 | 1                      | 9    | 30     |
--| 23 | 8                 | 11                     | 12   | 15     |
--| 53 | 8                 | 9                      | 15   | 20     |
--| 18 | 8                 | 6                      | 16   | 0      |
--+----+-------------------+------------------------+------+--------+


-- check if passenger link to the crime
SELECT * FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE year=2024 AND month=7 AND day=29 ORDER BY hour, minute LIMIT 1);

--+-----------+-----------------+------+
--| flight_id | passport_number | seat |
--+-----------+-----------------+------+
--| 36        | 7214083635      | 2A   |
--| 36        | 1695452385      | 3B   |
--| 36        | 5773159633      | 4A   |
--| 36        | 1540955065      | 5C   |
--| 36        | 8294398571      | 6C   |
--| 36        | 1988161715      | 6D   |
--| 36        | 9878712108      | 7A   |
--| 36        | 8496433585      | 7B   |
--+-----------+-----------------+------+

--cross ref with people passport number
SELECT * FROM people WHERE passport_number IN (
  SELECT passport_number FROM passengers WHERE flight_id = (SELECT id FROM flights WHERE year=2024 AND month=7 AND day=29 ORDER BY hour, minute LIMIT 1)
);

--+--------+--------+----------------+-----------------+---------------+
--|   id   |  name  |  phone_number  | passport_number | license_plate |
--+--------+--------+----------------+-----------------+---------------+
--| 395717 | Kenny  | (826) 555-1652 | 9878712108      | 30G67EN       |
--| 398010 | Sofia  | (130) 555-0289 | 1695452385      | G412CB7       |
--| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       |
--| 467400 | Luca   | (389) 555-5198 | 8496433585      | 4328GD8       |
--| 560886 | Kelsey | (499) 555-9472 | 8294398571      | 0NTHK55       |
--| 651714 | Edward | (328) 555-1152 | 1540955065      | 130LD9Z       |
--| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
--| 953679 | Doris  | (066) 555-9701 | 7214083635      | M51FA04       |
--+--------+--------+----------------+-----------------+---------------+



-- Create a sql query to get all the people who took a fligth the next day and get the destination

SELECT DISTINCT people.name
FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON flights.destination_airport_id = airports.id
WHERE bakery_security_logs.year = 2024
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 10 AND 30
AND flights.year = 2024
AND flights.month = 7
AND flights.day = 29;
SELECT DISTINCT people.name
FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
JOIN passengers ON people.passport_number = passengers.passport_number
JOIN flights ON passengers.flight_id = flights.id
JOIN airports ON flights.destination_airport_id = airports.id
WHERE bakery_security_logs.year = 2024
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 10 AND 30
AND flights.year = 2024
AND flights.month = 7
AND flights.day = 29;

--+--------+
--|  name  |
--+--------+
--| Diana  |
--| Sofia  |
--| Bruce  |
--| Kelsey |
--| Luca   |
--| Sophia |
--+--------+

-- modify my query so I also get the voyage and destination of each person
SELECT DISTINCT
people.name,
origin_airport.full_name AS origin_airport,
destination_airport.full_name AS destination_airport,
destination_airport.city AS destination_city
FROM people
JOIN bakery_security_logs
ON people.license_plate = bakery_security_logs.license_plate
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON passengers.flight_id = flights.id
JOIN airports AS origin_airport
ON flights.origin_airport_id = origin_airport.id
JOIN airports AS destination_airport
ON flights.destination_airport_id = destination_airport.id
WHERE bakery_security_logs.year = 2024
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 10 AND 30
AND flights.year = 2024
AND flights.month = 7
AND flights.day = 29;

--+--------+-----------------------------+------------------------------+------------------+
--|  name  |       origin_airport        |     destination_airport      | destination_city |
--+--------+-----------------------------+------------------------------+------------------+
--| Diana  | Fiftyville Regional Airport | Logan International Airport  | Boston           |
--| Sofia  | Fiftyville Regional Airport | LaGuardia Airport            | New York City    |
--| Bruce  | Fiftyville Regional Airport | LaGuardia Airport            | New York City    |
--| Kelsey | Fiftyville Regional Airport | LaGuardia Airport            | New York City    |
--| Luca   | Fiftyville Regional Airport | LaGuardia Airport            | New York City    |
--| Sophia | Fiftyville Regional Airport | O'Hare International Airport | Chicago          |
--+--------+-----------------------------+------------------------------+------------------+

-- cross those suspect with phone recort
SELECT id, caller, receiver FROM phone_calls
WHERE year = 2024 AND month = 7 AND day = 28
AND duration < 60;

--+-----+----------------+----------------+
--| id  |     caller     |    receiver    |
--+-----+----------------+----------------+
--| 221 | (130) 555-0289 | (996) 555-8899 |
--| 224 | (499) 555-9472 | (892) 555-8872 |
--| 233 | (367) 555-5533 | (375) 555-8161 |
--| 251 | (499) 555-9472 | (717) 555-1342 |
--| 254 | (286) 555-6063 | (676) 555-6554 |
--| 255 | (770) 555-1861 | (725) 555-3243 |
--| 261 | (031) 555-6622 | (910) 555-3251 |
--| 279 | (826) 555-1652 | (066) 555-9701 |
--| 281 | (338) 555-6650 | (704) 555-2131 |
--+-----+----------------+----------------+

-- MOdify query so I get the name of the caller and receiver
SELECT
phone_calls.id,
caller_person.name AS caller_name,
receiver_person.name AS receiver_name
FROM phone_calls
JOIN people AS caller_person ON phone_calls.caller = caller_person.phone_number
JOIN people AS receiver_person ON phone_calls.receiver = receiver_person.phone_number
WHERE phone_calls.year = 2024
AND phone_calls.month = 7
AND phone_calls.day = 28
AND phone_calls.duration < 60;

--+-----+-------------+---------------+
--| id  | caller_name | receiver_name |
--+-----+-------------+---------------+
--| 221 | Sofia       | Jack          |
--| 224 | Kelsey      | Larry         |
--| 233 | Bruce       | Robin         |
--| 251 | Kelsey      | Melissa       |
--| 254 | Taylor      | James         |
--| 255 | Diana       | Philip        |
--| 261 | Carina      | Jacqueline    |
--| 279 | Kenny       | Doris         |
--| 281 | Benista     | Anna          |
--+-----+-------------+---------------+


-- Comprehensive Summary of evidence
-- Time : July 28, 2024 around 10:15 AM
-- Location: Humphrey Street Bakery
-- 3 witnesses:
                --RUTH
                --EUGENE
                --RAYMOND
-- TESTIMONY
--RUTH
      -- saw thief leave in a car within 10 minutes of the theft
      -- => I look at the exit logs around 10:15AM
--EUGENE
      -- saw the thief withdraw money earlier at the ATM on Leggett Street
      -- => I loo at the logs of the ATM on Leggett Street
--RAYMOND
      -- saw the thief making a call under 1 min and :
          -- mention of leaving Fiftyville the next day (July 29)
          -- Asking the ACCOMPLICE to buy plane tickets
-- Filtering Bakery exit  between 10:10 and  10:30
-- 9 people :
            -- Vanessa
            -- Barry
            -- Iman
            -- Sofia
            -- Luca
            -- Diana
            -- Kelsey
            -- Sophia
            -- Bruce
-- Filtering ATM withdraw
-- 4 people:
            -- Bruce
            -- Diana
            -- Luca
            -- Kelsey
-- Then I check who took a flight out Fiftyville the next day (Earliest Fligth 8:20am)
-- Flight 36 (Fiftyville -> LaGuardia Airport)
-- Cross reference with bakery people
-- 5 suspects:
            -- Bruce
            -- Diana
            -- Kelsey
            -- Luca
            -- Sofia
-- Finally I check phone call made under 1 min
            -- Sofia    ->  Jack
            -- Kelsey   ->  Larry
            -- Bruce    ->  Robin
            -- Kelsey   ->  Melissa
            -- Taylor   ->  James
            -- Diana    ->  Philip
            -- Carina   ->  Jacqueline
            -- Kenny    ->  Doris
            -- Benista  ->  Anna
-- Conclusion
-- NAME    | At bakery | ATM withdraw on Legget st.| short call | fligth early |
-- Sophia  |     V     |              X            |      X     |       V      |
-- Vanessa |     V     |              X            |      X     |       X      |
-- Bruce   |     V     |              V            |      V     |       V      |
-- Barry   |     V     |              X            |      X     |       X      |
-- Luca    |     V     |              V            |      X     |       V      |
-- sofia   |     V     |              X            |      V     |       V      |
-- Iman    |     V     |              V            |      X     |       X      |
-- Diana   |     V     |              V            |      V     |       V      |
-- Kelsey  |     V     |              X            |      V     |       V      |

-- the only suspect that match all the testimony Is bruce
-- So Bruce is the thief
-- Looking at Flight 36; he escaped to NYC
-- His accomplice is the receiver of his phone call.
-- Accomplice : Robin
