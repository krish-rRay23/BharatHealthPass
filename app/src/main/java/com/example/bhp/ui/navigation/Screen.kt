package com.example.bhp.ui.navigation

sealed class Screen(val route: String) {
    object Login : Screen("login")
    object RoleSelection : Screen("role_selection")
    
    // Patient Screens
    object PatientDashboard : Screen("patient_dashboard")
    object PatientProfile : Screen("patient_profile")
    object PatientQR : Screen("patient_qr")
    object PatientHistory : Screen("patient_history")
    object PatientConsent : Screen("patient_consent")
    object PatientUpload : Screen("patient_upload")

    // Hospital Screens
    object HospitalDashboard : Screen("hospital_dashboard")
    object HospitalScan : Screen("hospital_scan")
    object HospitalResult : Screen("hospital_result/{authId}") {
        fun createRoute(authId: String) = "hospital_result/$authId"
    }
    object HospitalInvoice : Screen("hospital_invoice/{authId}") {
        fun createRoute(authId: String) = "hospital_invoice/$authId"
    }
}