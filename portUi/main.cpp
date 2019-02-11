#include "portui.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    portUi w;
    w.show();

    return a.exec();
}
