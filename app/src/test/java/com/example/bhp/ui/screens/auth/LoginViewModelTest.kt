package com.example.bhp.ui.screens.auth

import com.example.bhp.data.remote.TokenResponse
import com.example.bhp.data.repository.AuthRepository
import io.mockk.coEvery
import io.mockk.mockk
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.test.*
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class LoginViewModelTest {

    private val repository: AuthRepository = mockk(relaxed = true)
    private lateinit var viewModel: LoginViewModel
    private val testDispatcher = UnconfinedTestDispatcher()

    @Before
    fun setup() {
        Dispatchers.setMain(testDispatcher)
        viewModel = LoginViewModel(repository)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun `verifyOtp with correct dev credentials emits success`() = runTest {
        viewModel.toggleDevMode(true)
        viewModel.otp = "123456"
        coEvery { repository.verifyToken(any()) } returns Result.success(TokenResponse("jwt", "refresh"))

        viewModel.onVerifyOtp()

        val event = viewModel.loginEvents.first()
        assert(event is LoginViewModel.LoginEvent.Success)
    }

    @Test
    fun `verifyOtp with incorrect credentials emits error`() = runTest {
        viewModel.toggleDevMode(true)
        viewModel.otp = "wrong"

        viewModel.onVerifyOtp()

        val event = viewModel.loginEvents.first()
        assert(event is LoginViewModel.LoginEvent.Error)
    }
}