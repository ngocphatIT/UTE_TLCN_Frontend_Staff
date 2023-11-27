from tkinter import *
from tkinter import ttk
class DataGridView():
    def __init__(self,master,IDColumns,showColumns=None,show='headings'):
        if showColumns is None:
            showColumns = IDColumns
        self.reverseSort=False
        self.IDColumns = []
        self.showColumns = []
        self.dataGridView=ttk.Treeview(master,columns=IDColumns,show=show)
        for i in range(len(IDColumns)):
            self.addColumn(IDColumns[i],showColumns[i])
    def _sortby(self, col):
        l = [(self.dataGridView.set(k, col), k) for k in self.dataGridView.get_children('')]
        self.reverseSort=not self.reverseSort
        l.sort(reverse=self.reverseSort)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            self.dataGridView.move(k, '', index)
    def search(self,column,value,mode='SHOW'):
        found=[]
        if mode=='SHOW':
            column=self.convertShowColumnToIDColumn(column)
        for i in self.dataGridView.get_children():
            rowValue=self.mappingIDColumn(self.dataGridView.item(i)['values'])
            if value in str(rowValue[column]):
                found.append(rowValue)
        self.removeAllData()
        self.addRows(found)
        

    def mappingIDColumn(self,data):
        temp={}
        for i in range(len(data)):
            temp[self.IDColumns[i]]=data[i]
        return temp
    def convertShowColumnToIDColumn(self,data):
        return self.IDColumns[self.showColumns.index(data)]
    def getSelectedItem(self,mode='MAP'):
        if mode=='ROW':
            return self.dataGridView.item(self.dataGridView.focus())
        elif mode=='MAP':
            return self.mappingIDColumn(self.dataGridView.item(self.dataGridView.focus())['values'])

    def removeAllData(self):
        self.dataGridView.delete(*self.dataGridView.get_children())
    def addColumn(self,IDColumn,showColumn=None):
        if showColumn is None:
            showColumn=IDColumn
        self.IDColumns.append(IDColumn)
        self.showColumns.append(showColumn)
        self.dataGridView.heading(IDColumn,text=showColumn,command=lambda:self._sortby(IDColumn))
    def addRow(self,row,mode='ID'):
        context=[]
        if mode=='SHOW':
            for i in self.showColumns:
                if i in row.keys():
                    context.append(row[i])
        else:
            for i in self.IDColumns:
                if i in row.keys():
                    context.append(row[i])
        self.dataGridView.insert("", "end", values=context)
    def addRows(self,rows):
        for row in rows:
            self.addRow(row)
    def pack(self,filter=None):
        if filter is not None:
            self.dataGridView.pack(filter)
        self.dataGridView.pack()