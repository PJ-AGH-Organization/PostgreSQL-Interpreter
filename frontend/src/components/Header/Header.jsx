import React from "react";
import { Play, Settings, Database } from "lucide-react";

const Header = ({ onExecute }) => {
  return (
    <header className="flex items-center justify-between px-4 py-2 bg-[#252526] border-b border-gray-700">
      <div className="flex items-center space-x-4">
        <div className="flex items-center space-x-2">
          <Database className="h-5 w-5 text-blue-400" />
          <span className="font-medium text-white">SQL Visual Canvas</span>
        </div>

        <div className="border-l border-gray-700 h-6"></div>

        <div className="relative">
          <select className="appearance-none bg-[#333333] text-white rounded px-3 py-1 pr-8 border border-gray-700 text-sm focus:outline-none focus:border-blue-500">
            <option>SQL</option>
          </select>
          <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-400">
            <svg className="fill-current h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20">
              <path d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" />
            </svg>
          </div>
        </div>
      </div>

      <div className="flex items-center space-x-2">
        <button
          onClick={onExecute}
          className="bg-green-600 hover:bg-green-700 text-white font-medium px-4 py-1 text-sm rounded flex items-center"
        >
          <Play className="mr-1 h-4 w-4" />
          Run
        </button>

        <button className="text-gray-400 hover:text-white p-1 rounded hover:bg-[#333333]">
          <Settings className="h-5 w-5" />
        </button>
      </div>
    </header>
  );
};

export default Header;