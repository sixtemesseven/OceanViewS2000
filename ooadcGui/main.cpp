#include "ooadcgui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    ooAdcGUI w;
    w.show();

    return a.exec();
}
