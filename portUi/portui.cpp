#include "portui.h"
#include "ui_portui.h"

portUi::portUi(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::portUi)
{
    ui->setupUi(this);
}

portUi::~portUi()
{
    delete ui;
}
