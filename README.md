# Stock Control

As part of a test, was asked to complete three individual tasks about a stock control system.

## Task 1

Create a program that allows a user to choose between two options:

1. Calculate a check digit for a seven digit code.
2. Check if an eigth digit code's check digit is valid.

_A check digit is a digit that is calculated from all previous digits that can help ensure the data was transferred correctly. In these tasks we are using GTIN-8 codes._

### Calculate check digit

The first option allows the user to input a code and will generate a valid check digit. In this context a check digit is calculate using the following alogrithm:

1. Add together all the individual digits with the following modifications:
   - Each digit occupying an odd position should first be multiplied by three.
2. Add nine to the sum.
3. Divide by ten removing any remainders.
4. Multiply by ten.
5. Subtract step one from this result.

For example:

1. The user inputs the code `1234567`.
2. Each digit occupying an odd position is multiplied by three and then all the digits are added together: `(1 * 3) + 2 + (3 * 3) + 4 + (5 * 3) + 6 + (7 * 3)`, which equals `60`.
3. We add nine to `60` which gives us `69`.
4. We floor divide `69` by ten which gives us `6`, which we multiply by ten to give us `60`.
5. We subtract the original addition from `60`, which gives us `60 - 60 = 0`, so in this case our check digit is `0`.

### Check if check digit is valid

The second option should allow a user to input a code which will tell if the check digit is valid using the following algorithm:

1. Add together all the individual digits with the following modifications:
   - Each digit occupying an odd position should first be multiplied by three.
2. Divide the result by ten and take the remainder. If there is a remainder, the code is invalid otherwise it is valid.

For example:

1. The user inputs the code `12345670`.
2. Each digit occupying an odd position is multiplied by three and then all the digits are added together: `(1 * 3) + 2 + (3 * 3) + 4 + (5 * 3) + 6 + (7 * 3) + 0`, which equals `60`.
3. We then divide `60` by ten and obtain the remainder which is `0`.
4. Therefore the code is valid.

## Task 2

Create a program that allows a user to input a product code, then searches through a file to see if the product exists. If the product exists, the user should be asked to insert a quantity and then should be added to a basket.
The user should be able to add more than one product to their basket and should be told the total price of their order.

## Task 3

Create a program that allows a user to view stock levels for items. The program should extract information from a file that indicates target stock for a product and how much it currently has. The program should calculate how much stock should be ordered in order to reach target stock levels.
