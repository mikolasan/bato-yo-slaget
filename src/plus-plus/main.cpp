#include <Python.h>

int
main(int argc, char *argv[])
{
  Py_SetProgramName(argv[0]);  /* optional but recommended */
  Py_Initialize();
  PyRun_SimpleString("import sys\n"
                     "sys.path.insert(0, '.')\n"
                     "from battleship.Game import Game\n"
                     "game = Game()\n"
                     "game.play()\n");
  Py_Finalize();
  return 0;
}
