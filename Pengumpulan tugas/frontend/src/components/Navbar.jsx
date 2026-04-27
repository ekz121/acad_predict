(Navbar → tampilan & kontrol dark mode)

import React from "react";
import { GraduationCap, Sun, Moon } from "lucide-react";

const Navbar = ({ darkMode, setDarkMode }) => {
  return (
    <nav className="flex items-center justify-between px-6 py-4 shadow-md bg-white dark:bg-gray-800">
      
      {/* Logo */}
      <div className="flex items-center gap-2 text-xl font-bold text-gray-800 dark:text-white">
        <GraduationCap className="w-6 h-6" />
        <span>AcadPredict</span>
      </div>

      {/* Dark Mode Toggle */}
      <button
        onClick={() => setDarkMode(!darkMode)}
        className="p-2 rounded-lg bg-gray-200 dark:bg-gray-700 hover:scale-105 transition"
      >
        {darkMode ? (
          <Sun className="w-5 h-5 text-yellow-400" />
        ) : (
          <Moon className="w-5 h-5 text-gray-800" />
        )}
      </button>
    </nav>
  );
};

export default Navbar;
