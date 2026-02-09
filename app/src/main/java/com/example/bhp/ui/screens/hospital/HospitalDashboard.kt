package com.example.bhp.ui.screens.hospital

import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CameraAlt
import androidx.compose.material.icons.filled.Devices
import androidx.compose.material.icons.filled.History
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController
import com.example.bhp.ui.navigation.Screen

@Composable
fun HospitalDashboard(
    navController: NavController,
    viewModel: HospitalViewModel = hiltViewModel()
) {
    var selectedTab by remember { mutableIntStateOf(0) }

    Scaffold(
        bottomBar = {
            if (viewModel.isDeviceApproved) {
                NavigationBar {
                    NavigationBarItem(
                        selected = selectedTab == 0,
                        onClick = { selectedTab = 0 },
                        icon = { Icon(Icons.Default.CameraAlt, "Scan") },
                        label = { Text("Scan") }
                    )
                    NavigationBarItem(
                        selected = selectedTab == 1,
                        onClick = { selectedTab = 1 },
                        icon = { Icon(Icons.Default.History, "Treatments") },
                        label = { Text("Treatments") }
                    )
                }
            }
        }
    ) { padding ->
        Box(modifier = Modifier.padding(padding).fillMaxSize()) {
            if (!viewModel.isDeviceApproved) {
                DeviceRegistrationSection(
                    isLoading = viewModel.isLoading,
                    onRegister = { viewModel.registerDevice() }
                )
            } else {
                when (selectedTab) {
                    0 -> ScanSection(onScanClick = { navController.navigate(Screen.HospitalScan.route) })
                    1 -> TreatmentHistorySection()
                }
            }
        }
    }
}

@Composable
fun DeviceRegistrationSection(isLoading: Boolean, onRegister: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Icon(Icons.Default.Devices, contentDescription = null, modifier = Modifier.size(64.dp), tint = MaterialTheme.colorScheme.primary)
        Spacer(modifier = Modifier.height(16.dp))
        Text("Device Registration Required", style = MaterialTheme.typography.headlineSmall)
        Text(
            "This device must be approved by the backend before accessing operational features.",
            style = MaterialTheme.typography.bodyMedium,
            textAlign = androidx.compose.ui.text.style.TextAlign.Center
        )
        Spacer(modifier = Modifier.height(24.dp))
        Button(onClick = onRegister, enabled = !isLoading) {
            if (isLoading) {
                CircularProgressIndicator(modifier = Modifier.size(24.dp), color = MaterialTheme.colorScheme.onPrimary)
            } else {
                Text("Request Registration")
            }
        }
    }
}

@Composable
fun ScanSection(onScanClick: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Ready to Scan", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(32.dp))
        Button(
            onClick = onScanClick,
            modifier = Modifier.size(200.dp),
            shape = MaterialTheme.shapes.extraLarge
        ) {
            Column(horizontalAlignment = Alignment.CenterHorizontally) {
                Icon(Icons.Default.CameraAlt, contentDescription = null, modifier = Modifier.size(48.dp))
                Spacer(modifier = Modifier.height(12.dp))
                Text("Scan Patient QR")
            }
        }
    }
}

@Composable
fun TreatmentHistorySection() {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Active & Past Treatments", style = MaterialTheme.typography.headlineSmall)
        Spacer(modifier = Modifier.height(16.dp))
        // Placeholder for list of treatments
        Text("No active treatments found.", style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.secondary)
    }
}
