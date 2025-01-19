
import Chart from 'chart.js/auto';
import { Line } from 'react-chartjs-2';
import PropTypes from 'prop-types';



export default function ChartDate({ stats }) {

  const labels = stats.map(donation => new Date(donation.created_at).toLocaleDateString());

  const donationCounts = stats.reduce((acc, donation) => {
    const date = new Date(donation.created_at).toLocaleDateString();

    acc[date] = (acc[date] || 0) + 1;
    return acc;
  }, {});

  const data = {
    labels: Object.keys(donationCounts),
    datasets: [
      {
        label: 'Количество угощений',
        data: Object.values(donationCounts),
        fill: true,
        borderColor: '#ffb7008a',
   
        backgroundColor:'orange',
        tension: 0.1,
      },
    ],
  };


  return (

    <Line data={data} />

  )
}
