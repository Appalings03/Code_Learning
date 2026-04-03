#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all bitmap pixel from height
    for (int i = 0; i < height; i++)
    {
        // loop over all bitmap pixel from width
        for (int j = 0; j < width; j++)
        {
            int rgbt_gray =
                round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);

            // Set Red Green and Blue the same for each pixel of the bitmap
            image[i][j].rgbtRed = rgbt_gray;
            image[i][j].rgbtBlue = rgbt_gray;
            image[i][j].rgbtGreen = rgbt_gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all bitmap pixel from height
    for (int i = 0; i < height; i++)
    {
        // loop over all bitmap pixel from width
        for (int j = 0; j < width; j++)
        {
            // Create array to store RGBT Value adjusted for sepia color
            // 0 For Red
            // 1 For Green
            // 2 For Blue
            const int R = 0, G = 1, B = 2;
            int rgbt_sepia[3];
            rgbt_sepia[R] = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                                  .189 * image[i][j].rgbtBlue);
            rgbt_sepia[G] = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                                  .168 * image[i][j].rgbtBlue);
            rgbt_sepia[B] = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                                  .131 * image[i][j].rgbtBlue);

            // Verif that RGBT didn't go over 255
            for (int k = 0; k < 3; k++)
            {
                if (rgbt_sepia[k] >= 255)
                {
                    rgbt_sepia[k] = 255;
                }
            }

            // Adjust color for sepia filter
            image[i][j].rgbtRed = rgbt_sepia[R];
            image[i][j].rgbtGreen = rgbt_sepia[G];
            image[i][j].rgbtBlue = rgbt_sepia[B];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // loop over all bitmap pixel from height
    for (int i = 0; i < height; i++)
    {
        // loop over all bitmap pixel from width
        for (int j = 0; j < width / 2; j++)
        {
            // create temp image
            RGBTRIPLE tempImage = image[i][j];

            // invert each color
            tempImage.rgbtRed = image[i][width - 1 - j].rgbtRed;
            tempImage.rgbtGreen = image[i][width - 1 - j].rgbtGreen;
            tempImage.rgbtBlue = image[i][width - 1 - j].rgbtBlue;

            // Put new color in the new place
            image[i][width - 1 - j].rgbtRed = image[i][j].rgbtRed;
            image[i][width - 1 - j].rgbtGreen = image[i][j].rgbtGreen;
            image[i][width - 1 - j].rgbtBlue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = tempImage.rgbtRed;
            image[i][j].rgbtGreen = tempImage.rgbtGreen;
            image[i][j].rgbtBlue = tempImage.rgbtBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tempImage[height][width];
    const int R = 0, G = 1, B = 2;
    // loop over all bitmap pixel from height
    for (int i = 0; i < height; i++)
    {
        // loop over all bitmap pixel from width
        for (int j = 0; j < width; j++)
        {
            float count = 0;
            float pixelColor[3] = {0, 0, 0};

            for (int k = i - 1; k < i + 2; k++)
            {
                if (k >= 0 && k < height)
                {
                    for (int l = j - 1; l < j + 2; l++)
                    {
                        if (l >= 0 && l < width)
                        {
                            count++;
                            pixelColor[R] += image[k][l].rgbtRed;
                            pixelColor[G] += image[k][l].rgbtGreen;
                            pixelColor[B] += image[k][l].rgbtBlue;
                        }
                    }
                }
            }
            // adjust pixel color in temp Image
            tempImage[i][j].rgbtRed = round(pixelColor[R] / count);
            tempImage[i][j].rgbtGreen = round(pixelColor[G] / count);
            tempImage[i][j].rgbtBlue = round(pixelColor[B] / count);
        }
    }
    // Put new pixel color in the immage
    for (int i = 0; i < height; i++)
    {
        // loop over all bitmap pixel from width
        for (int j = 0; j < width; j++)
        {
            image[i][j] = tempImage[i][j];
        }
    }
    return;
}
