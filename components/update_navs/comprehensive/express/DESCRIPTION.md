This app demonstrates several key aspects of `update_navs()`:

1. **Panel Selection**: 
   - Selecting a specific panel using the "Select Panel" option
   - Resetting to the first panel
   - Cycling through panels

2. **Dynamic Navigation**:
   - Uses a radio button to control navigation updates
   - Showcases how `update_navs()` can change the selected panel programmatically

3. **Synthetic Data**:
   - Created mock navigation panels with different content
   - No external files used for data

4. **Reactive Context**:
   - Uses `@reactive.effect` and `@reactive.event` to trigger navigation updates
   - Shows how navigation can be dynamically controlled based on user interactions

5. **Additional Features**:
   - Displays the currently selected panel
   - Uses `navset_card_pill` for an attractive navigation interface

Key Points about `update_navs()`:
- Takes two primary parameters: 
  1. `id`: The ID of the navigation container
  2. `selected`: The value of the panel to select
- Works with various navigation containers like `navset_card_pill`, `navset_tab`, etc.
- Can be used to programmatically change the selected panel

Recommended Improvements/Variations:
1. Add more complex navigation logic
2. Implement panel-specific actions
3. Add more interactive elements to demonstrate navigation updates
## Preview the app on [Shinylive](https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXAAjFADugdOgnmAGlQGMB7CAFzkqVQDMAnUmZAZwAsBLCXZTmdKQYVkDOFGIVOANzgAdCI2ZsuPLHAAe6Ma1Z8BQkd3QBXCkROciYiABM4DBQoDEyAMq5K7OFOLJbUBRQyHRC-nAw5KwUDIGc5ArQ0gD6AUHIALzIIArIechyYOhQEHAANgCMhSg5YFIUZfK0hW5QjXoAIoFQhUSFZJTUFNUFYAAqpEFlbG1wehRcegCOJlDCDigAJACsAAy7BPu7hQC+BLn5hcWlZQBMI7X1jSOFALJrANY+3ADmyACSEFYnB+7AorF6owGVEoLzAAGFYMUQRBROJiOwUBUsLdkDBOGUyvFUSZWA4IWAzhc8lcSuUAMwPQpPJooQrw0kUZgOZCvHwMTjECl9MDQoZwjnRbkMGZSVh0CRScgoACctwApKdzqjLkU6WUACxMuqcBqs0YABSYthMkmQFocoQYMBKxCaIrFsOa41I6GQ2lINskKDcLuEyAA6oEMcgABpa6mja7lbbGllwgBi3FdnDayAA8rIGNJOHAAO6Q-rkGHDb1W0h0U14tY-bgoenbTWUhQnJwQVwWqA-ODIX1KoEKSw4IdwZJj1gAChZGUKADkoCWfnFyMgAKroNIjjoRUiQxuEqAAI0aGTGDBMcAAlH3XG5OPZL2tkGXTexkNCmDKCEIB-BZkCnYEPzWBdH0QRMp2MMxkliWx4mSS8zC5IEF0TfJRiSZIANIQkHErHU8JpMB103bdUXhatAMaRxCAKciKIxUhBTmDJgFwijKLcco4DtQcbjI-j+MKAAlOYfGQLlkCzBhonEiS8PZXBiEae19WFVi1PUsAOk4Vgr0aAB6ABRaBrxHUTygpPi8gAXUTZ8IBcZBqJBWi2Dk0C-xgEwyikdBtOTICFAC8DOCwJIyQoQi1lsZJ0AJMoF3fFcwHsSJkninxClgxMnWQL5cCICLkm4UI+FRAi0igLBTQiRdirYvDoqnAiIoXKqatIXiTTNQpnKIaQ2gfDJyvagz8inMMPlsUgywgBc6EKZxXBAfrFEGgByFl9uc3swHcua8indA+v1aq9qGz1a2c9zPJkxUZBHOA6DoYTwXk0hwkiIEYkCEcTAPUH8o3PQ6BMCBJGJNpTVwBQAAExHe2R1G+360YxhGsbgWRKEyiBTAoOKN0IhjiKY9z7DocCIaoKGaPHGC4LYoiSJlLJEIpgjuaYmDE0TThGaFnkMiyFohJE-Vqic5BXzlkRglYdBhPFwV-QVjr5ti8HD1ZxdCly0gTcKliyUaSQ4FsbKIsZM7RbY8pxf-GmecyGWwBkhL-sUzhlNrTm1Ncf25IUhYR0bEPdbE-XLsN5nZ3inCcpPS3ayIG3fvtx39SqF22MTd2Ja9pifdGeFNO0+zIqQJXXFrrSRwWJgTFBBOHOQJdFj4PR1f4MKTN8QGohB8dzok4gTAYGxEoivQsiJaIFwa7osHKtqZ-4ueF6GO77A0TJ-3nxfUt05q7E0Unyawc3s5gveKNKDREu4E+z4XA-L6-zQyAADUyAKiPmQOqZAjQ1p-yPsvV+eF35L31GfWBlAr43FYMAJBx9NCuSTjFLARtIbpzNlnAqOc-K2yoA7HBEVX5lyJBXSgjEpa+2MqZWyVkbL110orAhrgxgD3NsDWIVA9DsBWsgXApATB4hBGCfwnhYCCjaGUXgLpoDDh7tMEswJLwEmRkrKcxCWakMznlChkI852wdrSG4xcXr9mQBwsKUBeAx3PofSgVD862B0SEMIIjohiOJHjag9gGBYCoB-BQDMVArUIhfOB+oOaJjEBQeeqINoImST4huNR+aP3IdDHwMFTqUiIOAaA8BaBgDECsYOEQhisGiR-FiopqxDDqQoF0FAwqTCJJeRIJgBAozJiUAIwElZ4UpM5IAA)
