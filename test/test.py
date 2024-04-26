using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace demo1
{
    static class HistogramDemo
    {
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new HistogramForm());
        }
    }
}
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace demo1
{
    public class HistogramDrawer
    {
        private int[] _data;
        private Rectangle _drawingArea;
        private int _barWidth;
        private int _barSpacing;

        public HistogramDrawer(int[] data, Rectangle drawingArea, int barSpacing)
        {
            _data = data;
            _drawingArea = drawingArea;
            _barSpacing = barSpacing;
            CalculateBarWidth();
        }

        private void CalculateBarWidth()
        {
            _barWidth = (_drawingArea.Width - (_data.Length - 1) * _barSpacing) / _data.Length;
            if (_barWidth < 1) _barWidth = 1; // 防止宽度过小  
        }

        public void Draw(Graphics g)
        {
            int maxValue = _data.Max();
            int barHeight = _drawingArea.Height;

            for (int i = 0; i < _data.Length; i++)
            {
                int barTop = _drawingArea.Bottom - (int)((double)_data[i] / maxValue * barHeight);
                int barLeft = _drawingArea.Left + i * (_barWidth + _barSpacing);
                int barBottom = Math.Max(barTop, _drawingArea.Top); // 确保底部不会低于绘图区域的顶部  

                using (SolidBrush brush = new SolidBrush(Color.Blue))
                {
                    try
                    {
                        checked
                        {
                            g.FillRectangle(brush, barLeft, barTop, _barWidth, barBottom - barTop);
                        }
                    }
                    catch (OverflowException ex)
                    {
                        Console.WriteLine("OverflowException caught: " + ex.Message);
                        // 在这里可以处理异常，比如记录日志、返回一个错误码等。  
                    }

                }
            }
        }
    }
}
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace demo1
{
    public partial class HistogramForm : Form
    {
        private HistogramDrawer _histogramDrawer;
        private Timer _updateTimer;
        private Random _random;
        private int[] _data;
        public HistogramForm()
        {
            InitializeComponent();
            InitializeHistogram();
        }
        private void InitializeHistogram()
        {
            _random = new Random();
            _data = new int[10]; // 假设有10个数据点  
            _updateTimer = new Timer();
            _updateTimer.Interval = 1000; // 每秒更新一次数据  
            _updateTimer.Tick += UpdateDataAndRefresh;
            _updateTimer.Start();

            // 设定绘图区域（这里假设绘图区域占据整个窗体客户区）  
            Rectangle drawingArea = this.ClientRectangle;
            // 创建绘图类对象  
            _histogramDrawer = new HistogramDrawer(_data, drawingArea, 5); // 假设直方条之间间隔5个像素  
        }

        private void UpdateDataAndRefresh(object sender, EventArgs e)
        {
            // 更新数据（这里我们简单地生成随机数）  
            for (int i = 0; i < _data.Length; i++)
            {
                _data[i] = _random.Next(0, 100);
            }
            // 刷新窗体以重新绘制直方图  
            this.Invalidate();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);
            // 调用绘图方法  
            _histogramDrawer.Draw(e.Graphics);
        }
    }
}
