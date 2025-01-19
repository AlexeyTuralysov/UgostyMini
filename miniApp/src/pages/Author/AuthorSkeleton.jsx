
import '../../app/styles/pages/Author/Author.scss'
import Skeleton from '@mui/material/Skeleton';

export default function AuthorSkeleton() {
    return (

        <div className='user-block-skeleton'>
            <div className='user-avatar-skeleton'>
                <Skeleton variant="circular"  height={90} />
            </div>
            <div className='user-name-skeleton'>
                <Skeleton width={100} height={20} />

            </div>
            <div className='user-stats-skeleton'>
                <Skeleton width={100} height={30} />

                <Skeleton width={100} height={30} />
                <Skeleton width={100} height={30} />

            </div>
        </div >



    )
}
