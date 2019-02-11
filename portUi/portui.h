#ifndef PORTUI_H
#define PORTUI_H

#include <QMainWindow>

namespace Ui {
class portUi;
}

class portUi : public QMainWindow
{
    Q_OBJECT

public:
    explicit portUi(QWidget *parent = nullptr);
    ~portUi();

private:
    Ui::portUi *ui;
};

#endif // PORTUI_H
