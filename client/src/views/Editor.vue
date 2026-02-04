<template>
  <div class="min-h-screen bg-stone-50 dark:bg-stone-950 transition-colors">
    <!-- Header -->
    <header class="border-b border-stone-200 dark:border-stone-800">
      <div
        class="mx-auto w-full max-w-7xl px-6 sm:px-8 flex items-center justify-between py-6"
      >
        <!-- Left -->
        <div class="flex items-center gap-4">
          <button
            @click="goBack"
            class="text-sm font-semibold cursor-pointer text-stone-600 dark:text-stone-400 hover:text-emerald-800 dark:hover:text-emerald-400 transition-colors"
          >
            ← Notes
          </button>

          <span class="text-stone-400 dark:text-stone-500">/</span>

          <span class="font-semibold text-stone-900 dark:text-stone-100">
            {{ title || "Untitled note" }}
          </span>
        </div>

        <!-- Actions -->
        <div class="flex items-center gap-3">
          <button
            @click="deleteNote"
            class="px-3 py-2 rounded-lg text-sm font-semibold cursor-pointer text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-900/40 hover:bg-rose-50 dark:hover:bg-rose-950/30 transition-all focus:outline-none focus:ring-2 focus:ring-rose-600"
          >
            Delete
          </button>

          <button
            @click="saveNote"
            class="px-4 py-2 rounded-lg font-bold text-sm cursor-pointer bg-emerald-800 hover:bg-emerald-900 text-emerald-50 focus:outline-none focus:ring-2 focus:ring-emerald-700 transition-all shadow-sm"
          >
            Save
          </button>
        </div>
      </div>
    </header>

    <!-- Editor -->
    <main>
      <div class="mx-auto w-full max-w-3xl px-6 sm:px-8 py-10">
        <!-- Title -->
        <input
          v-model="title"
          type="text"
          placeholder="Note title"
          class="w-full mb-6 bg-transparent text-3xl font-black tracking-tight text-stone-900 dark:text-stone-100 placeholder-stone-400 dark:placeholder-stone-500 focus:outline-none"
        />

        <!-- CKEditor -->
        <div class="prose prose-stone max-w-none bg-white px-6 py-4">
          <Ckeditor :editor="Editor" v-model="content" :config="editorConfig" />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { Ckeditor } from "@ckeditor/ckeditor5-vue";

import {
  ClassicEditor,
  Essentials,
  Paragraph,
  Heading,
  Bold,
  Italic,
  Link,
  List,
  BlockQuote,
} from "ckeditor5";

import "ckeditor5/ckeditor5.css";

// Editor
const Editor = ClassicEditor;

// State
const title = ref("");
const content = ref("");

// Config
const editorConfig = {
  plugins: [
    Essentials,
    Paragraph,
    Heading,
    Bold,
    Italic,
    Link,
    List,
    BlockQuote,
  ],
  toolbar: [
    "heading",
    "|",
    "bold",
    "italic",
    "link",
    "bulletedList",
    "numberedList",
    "blockQuote",
    "|",
    "undo",
    "redo",
  ],
  placeholder: "Start writing...",
  licenseKey: "GPL",
};

// Actions
const goBack = (): void => {
  console.log("Back to notes");
};

const saveNote = (): void => {
  console.log("Save note", {
    title: title.value,
    content: content.value,
  });
};

const deleteNote = (): void => {
  console.log("Delete note");
};
</script>

<style>
/* Editor height */
.ck-editor__editable {
  min-height: 60vh;
}

/* Let Tailwind own the container */
.ck.ck-editor__main > .ck-editor__editable {
  border: none;
  box-shadow: none;
  background: transparent;
}

/* Dark mode toolbar tweaks */
.dark .ck.ck-toolbar {
  background: #0c0a09;
  border-color: #44403c;
}

.dark .ck.ck-button {
  color: #e7e5e4;
}
</style>
