package com.example.bhp.ui.screens.hospital

import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CheckCircle
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import androidx.fragment.app.FragmentActivity
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController
import com.example.bhp.util.BiometricHelper

@Composable
fun HospitalResultScreen(
    authId: String,
    navController: NavController,
    viewModel: HospitalViewModel = hiltViewModel()
) {
    val result = viewModel.scanResult
    val context = LocalContext.current

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Authorization Result", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(32.dp))

        if (result != null) {
            Icon(
                Icons.Default.CheckCircle,
                contentDescription = null,
                modifier = Modifier.size(64.dp),
                tint = Color.Green
            )
            Spacer(modifier = Modifier.height(16.dp))
            
            Card(modifier = Modifier.fillMaxWidth()) {
                Column(modifier = Modifier.padding(16.dp)) {
                    DetailRow("Auth ID", result.auth_id)
                    DetailRow("Approved Amount", "$${result.approved_amount}")
                    DetailRow("Identity", result.identity_summary)
                    DetailRow("Confidence", "${(result.confidence * 100).toInt()}%")
                    DetailRow("Source", result.source)
                }
            }

            Spacer(modifier = Modifier.height(32.dp))

            Button(
                onClick = {
                    if (BiometricHelper.isBiometricAvailable(context)) {
                        BiometricHelper.showBiometricPrompt(
                            activity = context as FragmentActivity,
                            title = "Authorize Treatment",
                            subtitle = "Confirm start of treatment for ${result.identity_summary}",
                            onSuccess = { viewModel.startTreatment(authId) },
                            onError = { /* Handle error */ }
                        )
                    } else {
                        viewModel.startTreatment(authId)
                    }
                },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Start Treatment")
            }

            Spacer(modifier = Modifier.height(8.dp))

            OutlinedButton(
                onClick = { navController.popBackStack() },
                modifier = Modifier.fillMaxWidth()
            ) {
                Text("Done")
            }
        } else {
            Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
                CircularProgressIndicator()
                Text("Fetching authorization details...", modifier = Modifier.padding(top = 64.dp))
            }
        }
    }
}

@Composable
private fun DetailRow(label: String, value: String) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 4.dp),
        horizontalArrangement = Arrangement.SpaceBetween
    ) {
        Text(label, style = MaterialTheme.typography.labelLarge, color = MaterialTheme.colorScheme.secondary)
        Text(value, style = MaterialTheme.typography.bodyLarge)
    }
}
