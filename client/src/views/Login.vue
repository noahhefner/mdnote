<template>
  <div
    class="min-h-screen flex items-center justify-center bg-stone-50 dark:bg-stone-950 px-4 transition-colors duration-300"
  >
    <div
      class="max-w-md w-full space-y-8 p-10 bg-white dark:bg-stone-900 rounded-2xl shadow-xl border border-emerald-100/50 dark:border-emerald-900/30"
    >
      <div class="text-center">
        <h2
          class="text-4xl font-black tracking-tight text-emerald-950 dark:text-emerald-50"
        >
          mdnote
        </h2>
      </div>

      <form class="mt-10 space-y-6" @submit.prevent="handleLogin">
        <div class="space-y-4">
          <div>
            <label
              for="email-address"
              class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-1"
              >Email</label
            >
            <input
              v-model="email"
              id="email-address"
              name="email"
              type="email"
              required
              class="block w-full px-4 py-3 border border-stone-200 dark:border-stone-700 rounded-lg text-stone-900 dark:text-white placeholder-stone-400 dark:placeholder-stone-500 focus:ring-2 focus:ring-emerald-700 focus:border-transparent bg-stone-50 dark:bg-stone-800 transition-all outline-none"
              placeholder="you@example.com"
            />
          </div>
          <div>
            <label
              for="password"
              class="block text-sm font-medium text-stone-700 dark:text-stone-300 mb-1"
              >Password</label
            >
            <input
              v-model="password"
              id="password"
              name="password"
              type="password"
              required
              class="block w-full px-4 py-3 border border-stone-200 dark:border-stone-700 rounded-lg text-stone-900 dark:text-white placeholder-stone-400 dark:placeholder-stone-500 focus:ring-2 focus:ring-emerald-700 focus:border-transparent bg-stone-50 dark:bg-stone-800 transition-all outline-none"
              placeholder="••••••••"
            />
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember-me"
              type="checkbox"
              class="h-4 w-4 text-emerald-800 border-stone-300 dark:border-stone-600 rounded focus:ring-emerald-700 dark:bg-stone-800 cursor-pointer"
            />
            <label
              for="remember-me"
              class="ml-2 block text-sm text-stone-600 dark:text-stone-400 cursor-pointer select-none"
            >
              Keep me logged in
            </label>
          </div>

          <div class="text-sm">
            <a
              href="#"
              class="font-semibold text-emerald-800 dark:text-emerald-400 hover:text-emerald-700 dark:hover:text-emerald-300 cursor-pointer underline-offset-4 hover:underline"
            >
              Forgot?
            </a>
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-bold rounded-lg text-white bg-emerald-800 hover:bg-emerald-900 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-emerald-700 transition-all shadow-md disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer"
            :disabled="isLoading"
          >
            <span v-if="isLoading">Authenticating...</span>
            <span v-else>Login</span>
          </button>
        </div>
      </form>

      <div class="mt-8 text-center text-sm">
        <span class="text-stone-500 dark:text-stone-400">New here?</span>
        <button
          class="ml-1 font-bold text-emerald-800 dark:text-emerald-400 hover:text-emerald-700 dark:hover:text-emerald-300 cursor-pointer underline-offset-4 hover:underline"
        >
          Create an account
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

// Define reactive state with explicit types
const email = ref<string>("");
const password = ref<string>("");
const rememberMe = ref<boolean>(false);
const isLoading = ref<boolean>(false);

/**
 * Handles the login submission
 */
const handleLogin = async (): Promise<void> => {
  if (!email.value || !password.value) return;

  isLoading.value = true;

  try {
    // Simulate API call
    console.log("Authenticating:", {
      email: email.value,
      remember: rememberMe.value,
    });

    await new Promise((resolve) => setTimeout(resolve, 1200));

    // Add your routing logic here, e.g., router.push('/dashboard')
  } catch (error) {
    console.error("Login failed:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>
