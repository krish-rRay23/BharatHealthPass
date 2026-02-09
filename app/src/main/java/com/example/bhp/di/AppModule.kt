package com.example.bhp.di

import android.content.Context
import androidx.room.Room
import androidx.work.WorkManager
import com.example.bhp.data.local.BHPDatabase
import com.example.bhp.data.local.SecurityManager
import com.example.bhp.data.remote.BHPService
import com.example.bhp.data.remote.TokenAuthenticator
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import okhttp3.Interceptor
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import javax.inject.Singleton
import javax.inject.Provider

@Module
@InstallIn(SingletonComponent::class)
object AppModule {

    @Provides
    @Singleton
    fun provideOkHttpClient(
        securityManager: SecurityManager,
        authenticator: TokenAuthenticator
    ): OkHttpClient {
        val logging = HttpLoggingInterceptor().apply {
            level = HttpLoggingInterceptor.Level.BODY
        }
        val authInterceptor = Interceptor { chain ->
            val request = chain.request().newBuilder()
            securityManager.getJwt()?.let {
                request.addHeader("Authorization", "Bearer $it")
            }
            chain.proceed(request.build())
        }
        return OkHttpClient.Builder()
            .addInterceptor(logging)
            .addInterceptor(authInterceptor)
            .authenticator(authenticator)
            .build()
    }

    @Provides
    @Singleton
    fun provideRetrofit(okHttpClient: OkHttpClient): Retrofit {
        // Change this to your actual backend URL or http://10.0.2.2/ for local emulator testing
        val baseUrl = "https://replace-with-your-api.com/" 
        
        return Retrofit.Builder()
            .baseUrl(baseUrl)
            .client(okHttpClient)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }

    @Provides
    @Singleton
    fun provideBHPService(retrofit: Retrofit): BHPService {
        return retrofit.create(BHPService::class.java)
    }

    @Provides
    @Singleton
    fun provideTokenAuthenticator(
        securityManager: SecurityManager,
        apiProvider: Provider<BHPService>
    ): TokenAuthenticator {
        return TokenAuthenticator(securityManager, apiProvider)
    }

    @Provides
    @Singleton
    fun provideDatabase(@ApplicationContext context: Context): BHPDatabase {
        return Room.databaseBuilder(
            context,
            BHPDatabase::class.java,
            "bhp_db"
        ).build()
    }

    @Provides
    @Singleton
    fun provideSyncQueueDao(db: BHPDatabase) = db.syncQueueDao()

    @Provides
    @Singleton
    fun provideWorkManager(@ApplicationContext context: Context): WorkManager {
        return WorkManager.getInstance(context)
    }
}
