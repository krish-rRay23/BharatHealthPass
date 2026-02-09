package com.example.bhp.ui.screens.patient

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController

@Composable
fun PatientConsentScreen(
    navController: NavController,
    viewModel: PatientViewModel = hiltViewModel()
) {
    Column(modifier = Modifier.fillMaxSize().padding(16.dp)) {
        Text("Data Access Consents", style = MaterialTheme.typography.headlineMedium)
        Text("Manage who can access your health records.", style = MaterialTheme.typography.bodySmall)
        
        Spacer(modifier = Modifier.height(16.dp))

        LazyColumn(modifier = Modifier.weight(1f)) {
            items(viewModel.consents) { consent ->
                ConsentItem(
                    title = consent.title,
                    description = consent.description,
                    isGranted = consent.isGranted,
                    onToggle = { viewModel.grantConsent(consent.id) }
                )
                HorizontalDivider()
            }
        }
        
        Button(
            onClick = { navController.popBackStack() },
            modifier = Modifier.fillMaxWidth().padding(top = 16.dp)
        ) {
            Text("Done")
        }
    }
}

@Composable
fun ConsentItem(
    title: String,
    description: String,
    isGranted: Boolean,
    onToggle: (Boolean) -> Unit
) {
    ListItem(
        headlineContent = { Text(title) },
        supportingContent = { Text(description) },
        trailingContent = {
            Switch(
                checked = isGranted,
                onCheckedChange = onToggle
            )
        }
    )
}
