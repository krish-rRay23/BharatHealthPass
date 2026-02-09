package com.example.bhp.ui.screens.role

import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun RoleSelectionScreen(
    onPatientSelected: () -> Unit,
    onHospitalSelected: () -> Unit
) {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Text("Choose Your Mode", style = MaterialTheme.typography.headlineMedium)
        Spacer(modifier = Modifier.height(32.dp))

        Button(
            onClick = onPatientSelected,
            modifier = Modifier.fillMaxWidth().height(64.dp)
        ) {
            Text("Patient Mode")
        }

        Spacer(modifier = Modifier.height(16.dp))

        OutlinedButton(
            onClick = onHospitalSelected,
            modifier = Modifier.fillMaxWidth().height(64.dp)
        ) {
            Text("Hospital Operational Mode")
        }
    }
}