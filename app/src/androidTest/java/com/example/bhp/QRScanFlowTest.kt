package com.example.bhp

import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.test.ext.junit.runners.AndroidJUnit4
import com.example.bhp.ui.navigation.Screen
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

@RunWith(AndroidJUnit4::class)
class QRScanFlowTest {

    @get:Rule
    val composeTestRule = createAndroidComposeRule<MainActivity>()

    @Test
    fun testLoginAndNavigateToHospitalMode() {
        // Assume Dev Mode is on
        composeTestRule.onNodeWithText("Send OTP").performClick()
        composeTestRule.onNodeWithText("Verify OTP").performClick()

        // Select Hospital Mode
        composeTestRule.onNodeWithText("Hospital Operational Mode").performClick()

        // Check if on Hospital Dashboard
        composeTestRule.onNodeWithText("Device Registration Required").assertExists()
    }
}