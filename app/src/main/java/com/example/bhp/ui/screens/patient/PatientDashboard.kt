package com.example.bhp.ui.screens.patient

import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController
import com.example.bhp.data.remote.ProfileResponse
import com.example.bhp.util.QRGenerator

@Composable
fun PatientDashboard(
    navController: NavController,
    viewModel: PatientViewModel = hiltViewModel()
) {
    var selectedItem by remember { mutableIntStateOf(0) }
    val items = listOf("Home", "QR", "History", "Profile")
    val icons = listOf(Icons.Default.Home, Icons.Default.QrCode, Icons.Default.History, Icons.Default.Person)

    Scaffold(
        bottomBar = {
            NavigationBar {
                items.forEachIndexed { index, item ->
                    NavigationBarItem(
                        icon = { Icon(icons[index], contentDescription = item) },
                        label = { Text(item) },
                        selected = selectedItem == index,
                        onClick = { selectedItem = index }
                    )
                }
            }
        }
    ) { padding ->
        Box(modifier = Modifier.padding(padding)) {
            when (selectedItem) {
                0 -> PatientHomeScreen(viewModel.profile)
                1 -> PatientQRScreen(viewModel.qrToken?.token)
                2 -> PatientHistoryScreen(viewModel.history)
                3 -> PatientProfileScreen(viewModel.profile)
            }
            
            if (viewModel.isLoading) {
                CircularProgressIndicator(modifier = Modifier.align(Alignment.Center))
            }
        }
    }
}

@Composable
fun PatientHomeScreen(profile: ProfileResponse?) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Welcome, ${profile?.name ?: "Patient"}", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(16.dp))
        
        Card(modifier = Modifier.fillMaxWidth()) {
            Column(modifier = Modifier.padding(16.dp)) {
                Text("Identity Confidence: ${(profile?.identityConfidence?.times(100))?.toInt() ?: 0}%", style = MaterialTheme.typography.titleMedium)
                Text("Eligibility Level: ${profile?.eligibilityLevel ?: "Checking..."}", style = MaterialTheme.typography.bodyMedium)
                LinearProgressIndicator(
                    progress = { profile?.identityConfidence ?: 0f },
                    modifier = Modifier.fillMaxWidth().padding(top = 8.dp)
                )
                profile?.fallbackReasons?.let { reasons ->
                    if (reasons.isNotEmpty()) {
                        Spacer(modifier = Modifier.height(8.dp))
                        Text("Remarks: ${reasons.joinToString(", ")}", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.error)
                    }
                }
            }
        }
        
        Spacer(modifier = Modifier.height(16.dp))
        
        Button(onClick = { /* Navigate to upload */ }, modifier = Modifier.fillMaxWidth()) {
            Text("Upload Documents")
        }
    }
}

@Composable
fun PatientQRScreen(token: String?) {
    Column(
        horizontalAlignment = Alignment.CenterHorizontally,
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center
    ) {
        Text("Your Identification QR", style = MaterialTheme.typography.headlineSmall)
        Spacer(modifier = Modifier.height(32.dp))
        
        if (token != null) {
            val qrBitmap = remember(token) { QRGenerator.generateQRCode(token) }
            Image(
                bitmap = qrBitmap.asImageBitmap(),
                contentDescription = "QR Code",
                modifier = Modifier.size(250.dp)
            )
        } else {
            Box(modifier = Modifier.size(250.dp), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
            }
        }
        
        Spacer(modifier = Modifier.height(16.dp))
        Text("Scan at the hospital reception", style = MaterialTheme.typography.bodyMedium)
        Text("QR refreshes automatically", style = MaterialTheme.typography.bodySmall, color = MaterialTheme.colorScheme.secondary)
    }
}

@Composable
fun PatientHistoryScreen(history: List<com.example.bhp.data.remote.HistoryResponse>) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Treatment History", style = MaterialTheme.typography.headlineSmall)
        Spacer(modifier = Modifier.height(16.dp))
        history.forEach { item ->
            ListItem(
                headlineContent = { Text(item.treatment) },
                supportingContent = { Text("${item.date} • ${item.status}") },
                leadingContent = { Icon(Icons.Default.History, null) }
            )
            HorizontalDivider()
        }
    }
}

@Composable
fun PatientProfileScreen(profile: ProfileResponse?) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Profile Settings", style = MaterialTheme.typography.headlineSmall)
        Spacer(modifier = Modifier.height(16.dp))
        DetailRow("Name", profile?.name ?: "")
        DetailRow("Address", profile?.address ?: "")
        DetailRow("Emergency Contact", profile?.emergencyContact ?: "")
    }
}

@Composable
fun DetailRow(label: String, value: String) {
    Row(
        modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
        horizontalArrangement = Arrangement.SpaceBetween
    ) {
        Text(label, style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.secondary)
        Text(value, style = MaterialTheme.typography.bodyLarge)
    }
}
