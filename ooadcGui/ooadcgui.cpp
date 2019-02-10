#include "ooadcgui.h"
#include "ui_ooadcgui.h"

ooAdcGUI::ooAdcGUI(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ooAdcGUI)
{
    ui->setupUi(this);
}

ooAdcGUI::~ooAdcGUI()
{
    delete ui;
}

void ooAdcGUI::on_pushButton_clicked()
{

}
