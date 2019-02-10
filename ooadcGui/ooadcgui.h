#ifndef OOADCGUI_H
#define OOADCGUI_H

#include <QMainWindow>

namespace Ui {
class ooAdcGUI;
}

class ooAdcGUI : public QMainWindow
{
    Q_OBJECT

public:
    explicit ooAdcGUI(QWidget *parent = nullptr);
    ~ooAdcGUI();

private slots:
    void on_pushButton_clicked();

private:
    Ui::ooAdcGUI *ui;
};

#endif // OOADCGUI_H
