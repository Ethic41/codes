#include <stdio.h>
#include <stdlib.h>

char code[] = "\x31\xC0\x50\x68\x72\x74\x74\x70\x68\x27\x72\x24\x20\x68\x25\x24\x27\x23\x68\x27\x20\x70\x25\x68\x74\x73\x76\x78\x68\x76\x20
\x23\x24\x68\x20\x25\x73\x70\x68\x27\x24\x20\x25\x68\x73\x70\x79\x25\x68\x78\x23\x76\x22\x68\x71\x24\x27\x78\x68\x27\x22\x74
\x23\x68\x71\x22\x76\x70\x68\x76\x70\x23\x20\x68\x72\x74\x70\x76\x68\x24\x70\x70\x24\x68\x70\x73\x74\x23\x68\x79\x27\x72\x78
\x68\x25\x71\x74\x23\x68\x71\x76\x24\x27\x68\x24\x73\x79\x75\x68\x75\x77\x74\x73\x68\x76\x79\x72\x24\x68\x74\x27\x25\x24\x68
\x78\x71\x25\x22\x68\x79\x25\x25\x22\x68\x20\x23\x24\x73\x68\x23\x70\x71\x27\x68\x74\x71\x75\x70\x68\x74\x74\x79\x23\x68\x75
\x77\x70\x71\x68\x73\x77\x73\x71\x54\x5E\x8B\xFE\x8B\xD7\xFC\xB9\x80\x00\x00\x00\xBB\x41\x00\x00\x00\x31\xC0\x50\xAC\x33\xC3
\xAA\xE2\xFA\x54\x5E\xCC";

int main(int argc, char **argv){
  int (*func) ();
  func = (int (*)()) code;
  (int)(*func)();
}
