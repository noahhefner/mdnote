<template>
  <div class="min-h-screen bg-stone-50 dark:bg-stone-950 transition-colors">
    <!-- Header -->
    <header class="border-b border-stone-200 dark:border-stone-800">
      <div
        class="mx-auto w-full max-w-7xl px-6 sm:px-8 flex items-center gap-6 py-6"
      >
        <!-- App name -->
        <h1
          class="text-3xl font-black tracking-tight text-emerald-950 dark:text-emerald-50 shrink-0"
        >
          mdnote
        </h1>

        <!-- Search -->
        <div class="flex-1">
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search notes..."
            class="w-full px-4 py-2 rounded-lg border border-stone-200 dark:border-stone-700 bg-stone-50 dark:bg-stone-800 text-stone-900 dark:text-stone-100 placeholder-stone-400 dark:placeholder-stone-500 focus:outline-none focus:ring-2 focus:ring-emerald-700 transition-all"
          />
        </div>

        <!-- Actions -->
        <div class="flex items-center gap-3 shrink-0">
          <button
            @click="openSettings"
            class="px-3 py-2 rounded-lg text-sm font-semibold cursor-pointer text-stone-700 dark:text-stone-300 border border-stone-200 dark:border-stone-700 hover:bg-stone-100 dark:hover:bg-stone-800 transition-all focus:outline-none focus:ring-2 focus:ring-emerald-700"
          >
            Settings
          </button>

          <button
            @click="logout"
            class="px-3 py-2 rounded-lg text-sm font-semibold cursor-pointer text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-900/40 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition-all focus:outline-none focus:ring-2 focus:ring-rose-600"
          >
            Logout
          </button>

          <button
            @click="createNote"
            class="px-4 py-2 rounded-lg font-bold text-sm cursor-pointer bg-emerald-800 hover:bg-emerald-900 text-emerald-50 focus:outline-none focus:ring-2 focus:ring-emerald-700 transition-all shadow-sm"
          >
            New note
          </button>
        </div>
      </div>
    </header>

    <!-- Content -->
    <main>
      <div class="mx-auto w-full max-w-7xl px-6 sm:px-8 py-8">
        <!-- Notes list -->
        <div v-if="groupedNotes.length" class="space-y-10">
          <section
            v-for="section in groupedNotes"
            :key="section.letter"
            class="space-y-2"
          >
            <!-- A–Z header -->
            <h2
              class="text-sm font-bold uppercase tracking-widest text-stone-500 dark:text-stone-400"
            >
              {{ section.letter }}
            </h2>

            <!-- Notes -->
            <div class="space-y-2">
              <button
                v-for="note in section.notes"
                :key="note.id"
                @click="openNote(note.id)"
                class="w-full text-left px-4 py-3 rounded-lg cursor-pointer border border-stone-200 dark:border-stone-700 bg-white dark:bg-stone-900 hover:bg-emerald-50 dark:hover:bg-emerald-950/30 transition-all focus:outline-none focus:ring-2 focus:ring-emerald-700"
              >
                <div class="flex items-center justify-between">
                  <span
                    class="font-semibold text-stone-900 dark:text-stone-100"
                  >
                    {{ note.title }}
                  </span>

                  <span class="text-xs text-stone-500 dark:text-stone-400">
                    {{ formatDate(note.updatedAt) }}
                  </span>
                </div>
              </button>
            </div>
          </section>
        </div>

        <!-- Empty search state -->
        <div v-else-if="searchQuery" class="py-24 text-center">
          <p class="text-stone-500 dark:text-stone-400">
            No notes found for
            <span class="font-semibold text-stone-700 dark:text-stone-300">
              “{{ searchQuery }}”
            </span>
          </p>

          <button
            @click="searchQuery = ''"
            class="mt-4 font-bold cursor-pointer text-emerald-800 dark:text-emerald-400 hover:underline underline-offset-4"
          >
            Clear search
          </button>
        </div>

        <!-- Empty app state -->
        <div
          v-else
          class="py-24 text-center text-stone-500 dark:text-stone-400"
        >
          No notes yet.
          <button
            @click="createNote"
            class="ml-1 font-bold cursor-pointer text-emerald-800 dark:text-emerald-400 hover:underline underline-offset-4"
          >
            Create your first one
          </button>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";

type Note = {
  id: string;
  title: string;
  updatedAt: Date;
};

// Mock data
const notes = ref<Note[]>([
  { id: "1", title: "API ideas", updatedAt: new Date("2026-01-12") },
  { id: "2", title: "Daily journal", updatedAt: new Date("2026-02-01") },
  { id: "3", title: "Vue patterns", updatedAt: new Date("2026-01-28") },
  { id: "4", title: "Auth flow", updatedAt: new Date("2026-01-05") },
]);

const searchQuery = ref("");

// Filter notes by search
const filteredNotes = computed(() => {
  if (!searchQuery.value) return notes.value;

  return notes.value.filter((note) =>
    note.title.toLowerCase().includes(searchQuery.value.toLowerCase()),
  );
});

// Group notes A–Z
const groupedNotes = computed(() => {
  const map = new Map<string, Note[]>();

  [...filteredNotes.value]
    .sort((a, b) =>
      a.title.localeCompare(b.title, undefined, { sensitivity: "base" }),
    )
    .forEach((note) => {
      const letter = note.title.charAt(0).toUpperCase();
      if (!map.has(letter)) map.set(letter, []);
      map.get(letter)!.push(note);
    });

  return Array.from(map.entries()).map(([letter, notes]) => ({
    letter,
    notes,
  }));
});

const openNote = (id: string): void => {
  console.log("Open note:", id);
};

const createNote = (): void => {
  console.log("Create new note");
};

const openSettings = (): void => {
  console.log("Open settings");
};

const logout = (): void => {
  console.log("Logout");
};

const formatDate = (date: Date): string => {
  return date.toLocaleDateString(undefined, {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
};
</script>
