/*
UseCase:
--------
Sleep Debt Calculator
Did you know that giraffes sleep 4.6 hours a day? We humans need more than that. If we don’t sleep enough, we accumulate sleep debt. In this project we’ll calculate if you’re getting enough sleep each week using a sleep debt calculator.

The program will determine the actual and ideal hours of sleep for each night of the last week.

Finally, it will calculate, in hours, how far you are from your weekly sleep goal.
*/
const getSleepHours = day => {
    switch(day){
      case 'Monday':
        return 8;
        break;
      case 'Tuesday':
        return 5;
        break;
      case 'Wednesday':
        return 4;
        break;
      case 'Thursday':
        return 6;
        break;
      case 'Friday':
        return 9;
        break;
      case 'Saturday':
        return 3;
        break;
      case 'Sunday':
        return 7;
        break;
    }
  };
  // console.log(getSleepHours('Tuesday'));
  
  // const getActualSleepHours = () => {
  //    return getSleepHours('Monday') + getSleepHours('Tuesday') + getSleepHours('Wednesday') + getSleepHours('Thursday') + getSleepHours('Friday') + getSleepHours('Saturday') + getSleepHours('Sunday') 
  // };
  const getActualSleepHours = () => 6 + 7 + 9 + 8 + 5 + 10 + 11;
  // const getIdealSleepHours = () => {
  //   const idealHours = 8;
  //   return idealHours*7;
  // }
  const getIdealSleepHours = idealHours => idealHours * 7;
  // console.log(getActualSleepHours());
  // console.log(getIdealSleepHours());
  
  const calculateSleepDebt = () => {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours(8); 
    if (actualSleepHours === idealSleepHours){
        console.log("User got the perfect amount of sleep");
    }else if (actualSleepHours > idealSleepHours){
        console.log("User got more sleep than needed.");
    }else if (actualSleepHours < idealSleepHours){
        console.log("User should get some rest.");
    }
  }
  console.log(calculateSleepDebt());