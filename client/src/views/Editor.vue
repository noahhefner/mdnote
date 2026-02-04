<template>
  <div
    class="min-h-screen bg-stone-50 dark:bg-stone-950 text-stone-900 dark:text-stone-100 transition-colors"
  >
    <!-- Header -->
    <header
      class="sticky top-0 z-10 bg-stone-50/80 dark:bg-stone-950/80 backdrop-blur border-b border-stone-200 dark:border-stone-800"
    >
      <div
        class="mx-auto w-full max-w-7xl px-6 sm:px-8 flex items-center justify-between py-5"
      >
        <!-- Left -->
        <div class="flex items-center gap-4 min-w-0">
          <button
            class="text-sm font-semibold text-stone-600 dark:text-stone-400 hover:text-emerald-700 dark:hover:text-emerald-400 transition-colors"
          >
            ← Notes
          </button>

          <span class="text-stone-300 dark:text-stone-600">/</span>

          <span
            class="truncate font-semibold text-stone-900 dark:text-stone-100"
          >
            {{ title || "Untitled note" }}
          </span>
        </div>

        <!-- Actions -->
        <div class="flex items-center gap-3">
          <button
            class="px-3 py-2 rounded-lg text-sm font-semibold text-rose-700 dark:text-rose-400 border border-rose-200 dark:border-rose-900/40 hover:bg-rose-50 dark:hover:bg-rose-950/40 focus:outline-none focus:ring-2 focus:ring-rose-500 focus:ring-offset-2 dark:focus:ring-offset-stone-950 transition"
          >
            Delete
          </button>

          <button
            class="px-4 py-2 rounded-lg text-sm font-bold bg-emerald-700 hover:bg-emerald-800 text-white shadow-sm shadow-emerald-900/10 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 dark:focus:ring-offset-stone-950 transition"
          >
            Save
          </button>
        </div>
      </div>
    </header>

    <!-- Editor -->
    <main>
      <div class="mx-auto w-full max-w-7xl px-6 sm:px-8 py-12">
        <div
          class="rounded-2xl bg-white dark:bg-stone-900 shadow-sm ring-1 ring-stone-200 dark:ring-stone-800 px-6 sm:px-8 py-8"
        >
          <!-- Title -->
          <input
            v-model="title"
            type="text"
            placeholder="Note title"
            class="w-full mb-6 bg-transparent text-3xl sm:text-4xl font-extrabold tracking-tight text-stone-900 dark:text-stone-100 placeholder-stone-400 dark:placeholder-stone-500 focus:outline-none"
          />

          <!-- Toolbar -->
          <div
            class="mb-4 flex flex-wrap items-center gap-1 rounded-xl bg-stone-100 dark:bg-stone-800 border border-stone-200 dark:border-stone-700 p-1"
          >
            <!-- Bold -->
            <button
              @click="editor?.chain().focus().toggleBold().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('bold') }"
              title="Bold"
            >
              <i class="bi bi-type-bold"></i>
            </button>

            <!-- Italic -->
            <button
              @click="editor?.chain().focus().toggleItalic().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('italic') }"
              title="Italic"
            >
              <i class="bi bi-type-italic"></i>
            </button>

            <!-- Strikethrough -->
            <button
              @click="editor?.chain().focus().toggleStrike().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('strike') }"
              title="Strikethrough"
            >
              <i class="bi bi-type-strikethrough"></i>
            </button>

            <div class="mx-1 h-5 w-px bg-stone-300 dark:bg-stone-600" />

            <!-- Headings -->
            <button
              @click="editor?.chain().focus().toggleHeading({ level: 1 }).run()"
              class="toolbar-btn"
              :class="{
                'is-active': editor?.isActive('heading', { level: 1 }),
              }"
              title="Heading 1"
            >
              <i class="bi bi-type-h1"></i>
            </button>

            <button
              @click="editor?.chain().focus().toggleHeading({ level: 2 }).run()"
              class="toolbar-btn"
              :class="{
                'is-active': editor?.isActive('heading', { level: 2 }),
              }"
              title="Heading 2"
            >
              <i class="bi bi-type-h2"></i>
            </button>

            <button
              @click="editor?.chain().focus().toggleHeading({ level: 3 }).run()"
              class="toolbar-btn"
              :class="{
                'is-active': editor?.isActive('heading', { level: 3 }),
              }"
              title="Heading 3"
            >
              <i class="bi bi-type-h3"></i>
            </button>

            <div class="mx-1 h-5 w-px bg-stone-300 dark:bg-stone-600" />

            <!-- Lists -->
            <button
              @click="editor?.chain().focus().toggleBulletList().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('bulletList') }"
              title="Bullet list"
            >
              <i class="bi bi-list-ul"></i>
            </button>

            <button
              @click="editor?.chain().focus().toggleOrderedList().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('orderedList') }"
              title="Numbered list"
            >
              <i class="bi bi-list-ol"></i>
            </button>

            <div class="mx-1 h-5 w-px bg-stone-300 dark:bg-stone-600" />

            <!-- Blockquote -->
            <button
              @click="editor?.chain().focus().toggleBlockquote().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('blockQuote') }"
              title="Quote"
            >
              <i class="bi bi-quote"></i>
            </button>

            <!-- Code -->
            <button
              @click="editor?.chain().focus().toggleCode().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('code') }"
              title="Inline code"
            >
              <i class="bi bi-code"></i>
            </button>

            <button
              @click="editor?.chain().focus().toggleCodeBlock().run()"
              class="toolbar-btn"
              :class="{ 'is-active': editor?.isActive('codeBlock') }"
              title="Code block"
            >
              <i class="bi bi-braces"></i>
            </button>

            <div class="mx-1 h-5 w-px bg-stone-300 dark:bg-stone-600" />

            <!-- Undo / Redo -->
            <button
              @click="editor?.chain().focus().undo().run()"
              class="toolbar-btn"
              title="Undo"
            >
              <i class="bi bi-arrow-counterclockwise"></i>
            </button>

            <button
              @click="editor?.chain().focus().redo().run()"
              class="toolbar-btn"
              title="Redo"
            >
              <i class="bi bi-arrow-clockwise"></i>
            </button>
          </div>

          <editor-content :editor="editor" />
        </div>
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useEditor, EditorContent } from "@tiptap/vue-3";
import StarterKit from "@tiptap/starter-kit";

const editor = useEditor({
  content: "<p>I'm running Tiptap with Vue.js. 🎉</p>",
  extensions: [StarterKit],
  editorProps: {
    attributes: {
      class:
        "prose prose-stone dark:prose-invert prose-sm sm:prose lg:prose-lg max-w-none focus:outline-none",
    },
  },
});

// State
const title = ref("");
</script>

<style scoped>
.is-active {
  background-color: oklch(59.6% 0.145 163.225);
}

.toolbar-btn {
  padding: 0 1rem;
  border-radius: 4px;
}

.toolbar-btn i {
  font-size: 1.5rem;
}
</style>
