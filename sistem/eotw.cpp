// -*- mode: C++ ; c-file-style: "ellemtel" ; coding: utf-8 -*-
//
// © 2013–2020  Roland Sieker <ospalh@gmail.com>
// Licence: CC-BY-SA 4.0

#include <ctime>
#include <iostream>

int main()
{
   int size = sizeof(time_t);
   std::cout << "time_t ist " << size << " chars lang.\n";
   if (size == 4)
   {
      std::cout << "Das Ende naht!\n";
   }
   else if (size == 8)
   {
      std::cout <<  "Keine Panik!\n";
   }
   else
   {
      std::cout << "Huch!\n";
   }

   return 0;
}
