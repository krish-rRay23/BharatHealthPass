package com.example.bhp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.NavType
import androidx.navigation.navArgument
import com.example.bhp.ui.navigation.Screen
import com.example.bhp.ui.screens.auth.LoginScreen
import com.example.bhp.ui.screens.role.RoleSelectionScreen
import com.example.bhp.ui.screens.patient.PatientDashboard
import com.example.bhp.ui.screens.patient.PatientUploadScreen
import com.example.bhp.ui.screens.hospital.HospitalDashboard
import com.example.bhp.ui.screens.hospital.HospitalScanScreen
import com.example.bhp.ui.screens.hospital.HospitalResultScreen
import com.example.bhp.ui.theme.BHPTheme
import dagger.hilt.android.AndroidEntryPoint
import androidx.fragment.app.FragmentActivity

@AndroidEntryPoint
class MainActivity : FragmentActivity() { // Changed to FragmentActivity for Biometrics
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            BHPTheme {
                BHPApp()
            }
        }
    }
}

@Composable
fun BHPApp() {
    val navController = rememberNavController()
    Scaffold { innerPadding ->
        NavHost(
            navController = navController,
            startDestination = Screen.Login.route,
            modifier = Modifier.padding(innerPadding)
        ) {
            composable(Screen.Login.route) {
                LoginScreen(onLoginSuccess = {
                    navController.navigate(Screen.RoleSelection.route) {
                        popUpTo(Screen.Login.route) { inclusive = true }
                    }
                })
            }
            composable(Screen.RoleSelection.route) {
                RoleSelectionScreen(
                    onPatientSelected = { navController.navigate(Screen.PatientDashboard.route) },
                    onHospitalSelected = { navController.navigate(Screen.HospitalDashboard.route) }
                )
            }
            composable(Screen.PatientDashboard.route) {
                PatientDashboard(navController)
            }
            composable(Screen.PatientUpload.route) {
                PatientUploadScreen(navController)
            }
            composable(Screen.HospitalDashboard.route) {
                HospitalDashboard(navController)
            }
            composable(Screen.HospitalScan.route) {
                HospitalScanScreen(navController)
            }
            composable(
                route = Screen.HospitalResult.route,
                arguments = listOf(navArgument("authId") { type = NavType.StringType })
            ) { backStackEntry ->
                val authId = backStackEntry.arguments?.getString("authId") ?: ""
                HospitalResultScreen(authId, navController)
            }
        }
    }
}